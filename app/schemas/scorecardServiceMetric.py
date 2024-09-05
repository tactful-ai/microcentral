from typing import Optional
from pydantic import BaseModel 
from . import team, scoreCard, scoreCardMetrics, microservice

class scorecardServiceMetric(BaseModel):
    id: int
    name: str
    code: Optional[str] = None   
    description: str
    metrics: list[scoreCardMetrics.metric4scorecard]
    services: list[microservice.MicroserviceCreateApi]

    class Config:
        orm_mode = True

class scorecardServiceMetricCreate(scorecardServiceMetric):
    pass

# Properties to receive on microserviceScoreCard update
class scorecardServiceMetricUpdate(scorecardServiceMetric):
    pass
