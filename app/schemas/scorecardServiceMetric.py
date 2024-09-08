from typing import Optional
from pydantic import BaseModel 
from . import team, scoreCard, scoreCardMetrics, microservice

class scorecardServiceMetric(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None   
    description: Optional[str] = None
    metrics: Optional[list[scoreCardMetrics.metric4scorecard]] = []
    services: Optional[list[microservice.MicroserviceCreateApi]] = []

    class Config:
        orm_mode = True

class scorecardServiceMetricCreate(scorecardServiceMetric):
    pass

# Properties to receive on microserviceScoreCard update
class scorecardServiceMetricUpdate(scorecardServiceMetric):
    pass
