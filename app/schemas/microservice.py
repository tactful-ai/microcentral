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


# Properties to receive on microservice update
class MicroserviceUpdate(MicroserviceBase):
    pass


# Properties shared by models stored in DB
class MicroserviceInDBBase(MicroserviceBase):
    id: int
    name: str
    code: Optional[str] = None   
    description: str
    #teamId: uuid.UUID
    #add this line
    team_name: Optional[str] =None

    class Config:
        orm_mode = True


# Properties to return to client
class Microservice(MicroserviceInDBBase):
    pass


# Properties properties stored in DB
class MicroserviceInDB(MicroserviceInDBBase):
    pass
