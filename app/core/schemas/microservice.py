import uuid

from pydantic import BaseModel


class Microservice(BaseModel):
    id: int
    name: str
    code: str
    description: str
    teamId: uuid.UUID

    class Config:
        orm_mode = True


class MicroserviceCreate(BaseModel):
    name: str
    code: str
    description: str
    teamId: uuid.UUID

    class Config:
        orm_mode = True


class MicroserviceUpdate(MicroserviceCreate):
    pass
