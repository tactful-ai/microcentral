# this file needs a cleanup and some refactoring but it works for now

from enum import Enum

import yaml
from app.core.schemas.metric import MetricCreate
from app.core.schemas.microservice import MicroserviceCreate
from app.core.schemas.scorecard import ScorecardCreate
from app.core.schemas.scoreCardMetrics import ScoreCardMetricsCreate
from app.core.schemas.team import TeamCreate
from app.core.services import (MetricsService, MicroservicesService,
                               ScoreCardMetricsService, ScorecardsService,
                               TeamsService)
from pydantic import BaseModel
from sqlalchemy.orm import Session


class Team(BaseModel):
    name: str

class Service(BaseModel):
    name: str
    team: str
    description: str

class MetricType(Enum):
    integer = "integer"
    boolean = "boolean"

class Metric(BaseModel):
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
                self._lookupTables['teams'][team.name] = self._teamsService.create(TeamCreate(**team.dict(), token=""))

        if len(self._microservicesService .list()) == 0:
            for service in data.services:
                self._lookupTables['services'][service.name] =  self._microservicesService .create(MicroserviceCreate(**service.dict(), teamId= self._lookupTables['teams'][service.team].id))

        if len(self._metricsService.list()) == 0:
            for metric in data.metrics:
                self._lookupTables['metrics'][metric.area] = self._metricsService.create(MetricCreate(**metric.dict()))

        if len(self._scorecardsService.list()) == 0:
            for scorecard in data.scorecards:
                dbScorecard = self._scorecardsService.create(ScorecardCreate(name=scorecard.name, description=scorecard.description))
                for metric in scorecard.metrics:
                    self._scoreCardMetricsService.create(ScoreCardMetricsCreate(scorecardId=dbScorecard.id, metricId=self._lookupTables['metrics'][metric].id))
                self._lookupTables['scorecards'][scorecard.name] = dbScorecard

        self.db.close()


