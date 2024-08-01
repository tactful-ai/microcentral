from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class ServiceMetricBase(BaseModel):
    serviceId: Optional[int] = None
    metricId: Optional[int] = None
    value: Optional[float] = None
    date: Optional[datetime] = None


# Properties to receive on microservice creation
class ServiceMetricCreate(ServiceMetricBase):
    serviceId: int
    metricId: int
    value: float
    date: datetime


# Properties to receive on microservice update
class ServiceMetricUpdate(ServiceMetricBase):
    pass


# Properties shared by models stored in DB
class ServiceMetricInDBBase(ServiceMetricBase):
    id: int
    serviceId: int
    metricId: int
    value: float
    date: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class ServiceMetric(ServiceMetricInDBBase):
    pass


# Properties properties stored in DB
class ServiceMetricInDB(ServiceMetricInDBBase):
    pass
