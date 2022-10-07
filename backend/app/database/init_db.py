# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

# this file needs a cleanup and some refactoring but it works for now

from enum import Enum

import yaml
from app import crud, schemas
from app.core.security import create_access_token
from app.database import base  # noqa: F401
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


class SeederInput(BaseModel):
    teams: list[Team]
    services: list[Service]
    metrics: list[Metric]
    scorecards: list[ScoreCard]

    class Config:
        use_enum_values = True

class Seeder:
    def __init__(self, db: Session):
        self.db = db
        self._teamsService = crud.CRUDTeam(self.db)
        self._microservicesService = crud.CRUDMicroservice(self.db)
        self._metricsService = crud.CRUDMetric(self.db)
        self._scorecardsService = crud.CRUDScoreCard(self.db)
        self._scoreCardMetricsService = crud.CRUDScoreCardMetric(self.db)
        self._microserviceScoreCardService = crud.CRUDMicroserviceScoreCard(self.db)
        self._lookupTables = {
            "teams": {},
            "services": {},
            "metrics": {},
            "scorecards": {}
        }

    def seed(self, data: SeederInput):
        if len(self._teamsService.list()) == 0:
            for team in data.teams:
                db_team = self._teamsService.create(schemas.TeamCreate(**team.dict(), token=""))
                token = create_access_token(str(db_team.id))
                self._teamsService.update(db_team.id, schemas.TeamCreate(**team.dict(), token=token))
                self._lookupTables["teams"][team.name] = db_team

        if len(self._metricsService.list()) == 0:
            for metric in data.metrics:
                code = metric.name.replace(" ", "-").lower()
                self._lookupTables['metrics'][code] = self._metricsService.create(schemas.MetricCreate(**metric.dict(), code=code))

        if len(self._scorecardsService.list()) == 0:
            for scorecard in data.scorecards:
                dbScoreCard = self._scorecardsService.create(schemas.ScoreCardCreate(name=scorecard.name, description=scorecard.description))
                for metric in scorecard.metrics:
                    self._scoreCardMetricsService.create(schemas.ScoreCardMetricsCreate(scoreCardId=dbScoreCard.id, metricId=self._lookupTables['metrics'][metric.replace(" ", "-").lower()].id))
                self._lookupTables['scorecards'][scorecard.name] = dbScoreCard

        if len(self._microservicesService .list()) == 0:
            for service in data.services:
                code = service.name.replace(" ", "-").lower()
                db_service = self._microservicesService .create(schemas.MicroserviceCreate(**service.dict(), teamId=self._lookupTables['teams'][service.team].id, code=code))
                for scorecard in service.scorecards:
                    self._microserviceScoreCardService.create(schemas.MicroserviceScoreCardCreate(microserviceId=db_service.id, scoreCardId=self._lookupTables['scorecards'][scorecard].id))
                self._lookupTables['services'][code] = db_service

        self.db.close()





def init_db(db: Session) -> None:
    with open("/app/seed.yml") as f:
        data = yaml.safe_load(f)
        seeder = Seeder(db)
        seeder.seed(SeederInput(**data))

