from datetime import datetime

from pydantic import BaseModel


class ServiceMetric(BaseModel):
    id: int
    scorecard_id: int
    metric_id: int
    value: int
    timestamp: datetime

    class Config:
        orm_mode = True


class ServiceMetricCreate(ServiceMetric):
    scorecard_id: int
    metric_id: int
    value: int

    class Config:
        orm_mode = True


class ServiceMetricUpdate(ServiceMetricCreate):
    pass
