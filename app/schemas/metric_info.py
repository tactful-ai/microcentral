from pydantic import BaseModel 
from typing import Optional, Union
from datetime import datetime


class MetricInfoBase(BaseModel):
    metricId: int
    metricName : str
    value: Union[float, int, str, bool]
    timestamp: datetime
    weight:int
    
    class Config:
        orm_mode = True

