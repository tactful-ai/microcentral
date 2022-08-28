from typing import List, Optional

from pydantic import BaseModel

from .microservice import Microservice


class Team(BaseModel):
    id: int
    name: str
    services: List[Microservice] = []


    class Config:
        orm_mode = True


class TeamCreate(BaseModel):
    name: str
    services: Optional[List[Microservice]] = []

    class Config:
        orm_mode = True


class TeamUpdate(TeamCreate):
    pass
