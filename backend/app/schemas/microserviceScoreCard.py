from pydantic import BaseModel


class MicroserviceScoreCard(BaseModel):
    id: int
    microserviceId: int
    scorecardId: int

    class Config:
        orm_mode = True


class MicroserviceScoreCardCreate(BaseModel):
    microserviceId: int
    scorecardId: int

    class Config:
        orm_mode = True


class MicroserviceScoreCardUpdate(MicroserviceScoreCardCreate):
    pass
