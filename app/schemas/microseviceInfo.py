from pydantic import BaseModel
from typing import Optional
from . import scoreCard


class MicroserviceInfoBase(BaseModel):
    id: int
    name: str
    code: Optional[str] = None
    description: str
    team_name: str
    scorecards: list[scoreCard.ScoreCard]

    class Config:
        orm_mode = True
