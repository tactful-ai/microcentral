from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ServiceMetric(BaseModel):
    id: int
    serviceId: int
    metricId: int
    value: int
    timestamp: Optional[datetime] = None

    class Config:
        orm_mode = True


class ServiceMetricCreate(BaseModel):
    serviceId: int
    metricId: int
    value: int
    timestamp: Optional[datetime] = None

    class Config:
        orm_mode = True


class ServiceMetricUpdate(ServiceMetricCreate):
    pass
