from typing import List, Optional

from pydantic import BaseModel

from .microservice import Microservice


class Team(BaseModel):
    id: int
    name: str
    token: str
    services: List[Microservice] = []

    class Config:
        orm_mode = True


class TeamCreate(BaseModel):
    name: str
    token: str

    class Config:
        orm_mode = True


class TeamUpdate(TeamCreate):
    pass
