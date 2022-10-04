from pydantic import BaseModel


class Scorecard(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


class ScorecardCreate(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True

class ScorecardUpdate(ScorecardCreate):
    pass
