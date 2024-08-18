from typing import Optional , List

from pydantic import BaseModel 


# Shared properties
class MicroserviceScoreCardBase(BaseModel):
    microserviceId: Optional[int] = None
    scoreCardId: Optional[int] = None

#added 
class ScoreCardBase(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None

# Properties to receive on microserviceScoreCard creation
class MicroserviceScoreCardCreate(MicroserviceScoreCardBase):
    microserviceId: int
    scoreCardId: int


# Properties to receive on microserviceScoreCard update
class MicroserviceScoreCardUpdate(MicroserviceScoreCardBase):
    pass


# Properties shared by models stored in DB

class MicroserviceScoreCardInDBBase(MicroserviceScoreCardBase):
    id: int
    microserviceId: int
    scoreCardId: int

    class Config:
        orm_mode = True


# Properties to return to client
class MicroserviceScoreCard(MicroserviceScoreCardInDBBase):
    pass


# Properties properties stored in DB
class MicroserviceScoreCardInDB(MicroserviceScoreCardInDBBase):
    pass
