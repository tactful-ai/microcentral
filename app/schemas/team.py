import uuid
from typing import List, Optional

from pydantic import BaseModel

from .microservice import Microservice


# Shared properties
class TeamBase(BaseModel):
    name: Optional[str] = None
    token: Optional[str] = ""
    microservices: Optional[List[Microservice]] = []


# Properties to receive on team creation
class TeamCreate(TeamBase):
    name: str



# Properties to receive on team update
class TeamUpdate(TeamBase):
    pass


# Properties shared by models stored in DB
class TeamInDBBase(TeamBase):
    id: uuid.UUID
    name: str
    token: str
    microservices: List[Microservice]

    class Config:
        orm_mode = True


# Properties to return to client
class Team(TeamInDBBase):
    pass


# Properties properties stored in DB
class TeamInDB(TeamInDBBase):
    pass
