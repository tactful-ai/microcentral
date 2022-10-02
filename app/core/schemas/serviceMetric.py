from datetime import datetime

from pydantic import BaseModel


class ServiceMetric(BaseModel):
    id: int
    ServiceId: int
    metricId: int
    value: int
    timestamp: datetime

    class Config:
        orm_mode = True


class ServiceMetricCreate(ServiceMetric):
    ServiceId: int
    metricId: int
    value: int

    class Config:
        orm_mode = True


class ServiceMetricUpdate(ServiceMetricCreate):
    pass
