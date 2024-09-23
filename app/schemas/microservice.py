import uuid
from typing import Optional

from pydantic import BaseModel


# Shared properties
class MicroserviceBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    teamId: Optional[uuid.UUID] = None
    code: Optional[str] = None


# Properties to receive on microservice creation
class MicroserviceCreate(MicroserviceBase):
    name: str
    description: str
    code: str
    teamId:uuid.UUID
#new
class MicroserviceCreateApi(MicroserviceBase):
    name: str
    description: str
    teamId:Optional[uuid.UUID] = None
    scorecardids: Optional [list[int]] = None
    
    
    class Config:
        orm_mode = True

class Microserviceforscorecard(BaseModel):
    name: str
    description: str
    teamId:uuid.UUID = None
    id: int

    class Config:
        orm_mode = True
# Properties to receive on microservice update
class MicroserviceUpdate(MicroserviceBase):
    name: str
    description: str
    teamId: uuid.UUID
    
    class Config:
        orm_mode = True


# Properties shared by models stored in DB
class MicroserviceInDBBase(MicroserviceBase):
    id: int
    name: str
    code: str
    description: str
    teamId:uuid.UUID 
    team_name: Optional[str] =None
    scorecard_names: Optional[list] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Microservice(MicroserviceInDBBase):
    pass


# Properties properties stored in DB
class MicroserviceInDB(MicroserviceInDBBase):
    pass
