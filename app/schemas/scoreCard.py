from typing import Optional
from . import microservice, scoreCardMetrics, microservice
from pydantic import BaseModel
from datetime import datetime


# Shared properties
class ScoreCardBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None

# Properties to receive on scorecard creation
class ScoreCardCreate(BaseModel):
    name: str
    code : str
    description: str

# Properties to receive on scorecard update
class ScoreCardUpdate(ScoreCardBase):
    pass

# Properties shared by models stored in DB
class ScoreCardInDBBase(ScoreCardBase):
    id: int
    name: str
    code: str
    description: str

    class Config:
        orm_mode = True

class ScoreCardinBase(ScoreCardBase):
    id: int
    name: str
    code: str
    description: str
    services: list[microservice.MicroserviceCreate]
    metrics: list[scoreCardMetrics.ScoreCardMetricsCreate]

class GetScoreCard(BaseModel):
    id: int
    name: str
    code: str
    description: str
    services: list[microservice.MicroserviceBase]

class listScoreCard(BaseModel):
    id: int
    name: str
    code: str
    description: str
    services: list[microservice.Microserviceforscorecard]
    metrics: list[scoreCardMetrics.MetricListforScorecardGet]

# Properties to return to client
class ScoreCard(ScoreCardInDBBase):
    id: int
    name: str
    code: str
    update_time:Optional[datetime] = datetime.now() 
    score_value: float

    class Config:
        orm_mode = True


# Properties properties stored in DB
class ScoreCardInDB(ScoreCardInDBBase):
    pass
