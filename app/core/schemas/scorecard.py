from pydantic import BaseModel


class Scorecard(BaseModel):
    id: int
    name: str
    description: str
    microservice_id: int

    class Config:
        orm_mode = True


class ScorecardCreate(Scorecard):
    name: str
    description: str
    microservice_id: int

    class Config:
        orm_mode = True

class ScorecardUpdate(ScorecardCreate):
    pass
