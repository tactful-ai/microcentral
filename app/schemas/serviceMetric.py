from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel



# Shared properties
class ServiceMetricBase(BaseModel):
    serviceId: Optional[int] = None
    metricId: Optional[int] = None
    value: Optional[Union[float, int, str, bool]] = None
    date: Optional[datetime] = None


# Properties to receive on microservice creation
class ServiceMetricCreate(ServiceMetricBase):
    serviceId: int
    metricId: int
    value: Union[float, int, str, bool]
    date: datetime


# Properties to receive on microservice update
class ServiceMetricUpdate(ServiceMetricBase):
    pass


# Properties shared by models stored in DB
class ServiceMetricInDBBase(ServiceMetricBase):
    id: int
    serviceId: int
    metricId: int
    value: Union[float, int, str, bool]
    date: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class ServiceMetricReading(BaseModel):
    metricId: int
    value: Union[float, int, str, bool]
    timestamp: datetime

    class Config:
        orm_mode = True 


# Properties properties stored in DB
class ServiceMetricInDB(ServiceMetricInDBBase):
    pass
