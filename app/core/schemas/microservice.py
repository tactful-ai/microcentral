from pydantic import BaseModel


class Microservice(BaseModel):
    id: int
    name: str
    description: str
    teamId: int

    class Config:
        orm_mode = True


class MicroserviceCreate(BaseModel):
    name: str
    description: str
    teamId: int

    class Config:
        orm_mode = True


class MicroserviceUpdate(MicroserviceCreate):
    pass
