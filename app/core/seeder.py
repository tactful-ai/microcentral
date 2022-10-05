# this file needs a cleanup and some refactoring but it works for now

from enum import Enum

import yaml
from app.core.schemas import (MetricCreate, MicroserviceCreate,
                              MicroserviceScoreCardCreate, ScorecardCreate,
                              ScoreCardMetricsCreate, TeamCreate)
from app.core.services import (MetricsService, MicroserviceScoreCardService,
                               MicroservicesService, ScoreCardMetricsService,
                               ScorecardsService, TeamsService, signJWT)
from pydantic import BaseModel
from sqlalchemy.orm import Session


class Team(BaseModel):
    name: str

class Service(BaseModel):
    name: str
    team: str
    description: str
    scorecards: list[str]

class MetricType(Enum):
    integer = "integer"
    boolean = "boolean"

class Metric(BaseModel):
    name: str
    area: str
    description: str
    type: MetricType

    class Config:
        use_enum_values = True

class ScoreCard(BaseModel):
    name: str
    description: str
    metrics: list[str]


class Seed(BaseModel):
    teams: list[Team]
    services: list[Service]
    metrics: list[Metric]
    scorecards: list[ScoreCard]

    class Config:
        use_enum_values = True

class Seeder:
    def __init__(self, db: Session):
        self.db = db
        self._teamsService = TeamsService(self.db)
        self._microservicesService = MicroservicesService(self.db)
        self._metricsService = MetricsService(self.db)
        self._scorecardsService = ScorecardsService(self.db)
        self._scoreCardMetricsService = ScoreCardMetricsService(self.db)
        self._microserviceScoreCardService = MicroserviceScoreCardService(self.db)
        self._lookupTables = {
            "teams": {},
            "services": {},
            "metrics": {},
            "scorecards": {}
        }

    def seed(self):
        with open("/usr/src/app/app/services.yml", "r") as stream:
            try:
                data = yaml.safe_load(stream)
                self.run(Seed(**data))
            except yaml.YAMLError as exc:
                print(exc)

    def run(self, data: Seed):
        if len(self._teamsService.list()) == 0:
            for team in data.teams:
                db_team = self._teamsService.create(TeamCreate(**team.dict(), token=""))
                token = signJWT(str(db_team.id))
                print(f"Team {team.name} created with token {token}")
                self._teamsService.update(db_team.id, TeamCreate(**team.dict(), token=token))
                self._lookupTables["teams"][team.name] = db_team

        if len(self._metricsService.list()) == 0:
            for metric in data.metrics:
                code = metric.name.replace(" ", "-").lower()
                self._lookupTables['metrics'][code] = self._metricsService.create(MetricCreate(**metric.dict(), code=code))

        if len(self._scorecardsService.list()) == 0:
            for scorecard in data.scorecards:
                dbScorecard = self._scorecardsService.create(ScorecardCreate(name=scorecard.name, description=scorecard.description))
                for metric in scorecard.metrics:
                    self._scoreCardMetricsService.create(ScoreCardMetricsCreate(scorecardId=dbScorecard.id, metricId=self._lookupTables['metrics'][metric.replace(" ", "-").lower()].id))
                self._lookupTables['scorecards'][scorecard.name] = dbScorecard

        if len(self._microservicesService .list()) == 0:
            for service in data.services:
                code = service.name.replace(" ", "-").lower()
                db_service = self._microservicesService .create(MicroserviceCreate(**service.dict(), teamId=self._lookupTables['teams'][service.team].id, code=code))
                for scorecard in service.scorecards:
                    self._microserviceScoreCardService.create(MicroserviceScoreCardCreate(microserviceId=db_service.id, scorecardId=self._lookupTables['scorecards'][scorecard].id))
                self._lookupTables['services'][code] = db_service

        self.db.close()


