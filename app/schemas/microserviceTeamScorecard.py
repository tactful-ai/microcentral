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



class MicroserviceTeamScorecardUpdate(MicroserviceTeamScorecardBase):
    pass