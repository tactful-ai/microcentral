from pydantic import BaseModel


class Microservice(BaseModel):
    id: int
    name: str
    description: str
    team_id: int

    class Config:
        orm_mode = True


class MicroserviceCreate(BaseModel):
    name: str
    description: str
    team_id: int

    class Config:
        orm_mode = True


class MicroserviceUpdate(MicroserviceCreate):
    pass