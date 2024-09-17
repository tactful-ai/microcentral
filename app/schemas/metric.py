from typing import Optional, List 

from pydantic import BaseModel, validator


# Shared properties
class MetricBase(BaseModel):
    id: Optional[int] = None
    name:  Optional[str] = None
    code:  Optional[str] = None
    area:  Optional[List[str]] = None
    description: Optional[str] = None
    type: Optional[str] = None

    

# Properties to receive on metric creation
class MetricCreate(MetricBase):
    name: str
    description: str
    type: str

class MetricGet(MetricBase):
    area: Optional[str] = None

# Properties to receive on metric update
class MetricUpdate(MetricBase):
    pass

# Properties shared by models stored in DB
class MetricInDBBase(MetricBase):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True

# Properties to return to client
class Metric(MetricInDBBase):
  pass
   

# Properties properties stored in DB
class MetricInDB(MetricInDBBase):
    pass
