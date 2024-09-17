from typing import Optional
from pydantic import BaseModel 
from . import team, scoreCard, scoreCardMetrics, microservice

class scorecardServiceMetric(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None   
    description: Optional[str] = None
    metrics: Optional[list[scoreCardMetrics.MetricListforScorecardGet]] = []
    services: Optional[list[microservice.Microserviceforscorecard]] = []

    class Config:
        orm_mode = True

class scorecardServiceMetricCreate(scorecardServiceMetric):
    name: str
    description: str
    # Here i will get the name of the services then search by code 
    # to get the id of the service and update the microservicescorecard table
    services: Optional[list[int]] = []
    metrics: Optional[list[scoreCardMetrics.metricCreateScorecard]] = []


# Properties to receive on microserviceScoreCard update
class scorecardServiceMetricUpdate(scorecardServiceMetric):
    pass
