from typing import Optional
from . import microservice, scoreCardMetrics, microservice
from pydantic import BaseModel


# Shared properties
class ScoreCardBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None
    services: list[microservice.MicroserviceCreateApi]
    metrics: list[scoreCardMetrics.ScoreCardMetricsCreate]

# Properties to receive on scorecard creation
class ScoreCardCreate(ScoreCardBase):
    name: str
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
    services: list[microservice.MicroserviceCreate]
    metrics: list[scoreCardMetrics.ScoreCardMetricsCreate]

    class Config:
        orm_mode = True

class GetScoreCard(ScoreCardBase):
    id: int
    services: microservice.MicroserviceBase

# Properties to return to client
class ScoreCard(ScoreCardInDBBase):
    pass

# Properties properties stored in DB
class ScoreCardInDB(ScoreCardInDBBase):
    pass
