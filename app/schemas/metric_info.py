from pydantic import BaseModel 
from typing import Optional
from datetime import datetime
from . import serviceMetric

class MetricInfoBase(BaseModel):
    serviceId: int
    metricId: int
    value: float
    date: datetime
    
    class Config:
        orm_mode = True


class MicroserviceInfoCreate(MetricInfoBase):
    pass


class MicroserviceInfoUpdate(MetricInfoBase):
    pass