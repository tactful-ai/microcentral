from typing import Optional
from pydantic import BaseModel 
from . import team ,scoreCard

class MicroserviceTeamScorecardBase(BaseModel):
    id: int
    name: str
    code: Optional[str] = None   
    description: str
    team:team.TeamBase 
    scorecards:list[scoreCard.ScoreCardInDBBase]

    class Config:
        orm_mode = True

class MicroserviceTeamScorecardCreate(MicroserviceTeamScorecardBase):
    pass


# Properties to receive on microserviceScoreCard update
class MicroserviceTeamScorecardUpdate(MicroserviceTeamScorecardBase):
    pass