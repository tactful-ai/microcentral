from typing import Optional
from pydantic import BaseModel
from datetime import datetime


# Shared properties
class ScoreCardBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

# Properties to receive on scorecard creation
class ScoreCardCreate(ScoreCardBase):
    name: str
    description: str

# Properties to receive on scorecard update
class ScoreCardUpdate(ScoreCardBase):
    pass

# Properties shared by models stored in DB
class ScoreCardInDBBase(ScoreCardBase):
    id: int
    name: str
    code: str
    description: Optional[str]= None

    class Config:
        orm_mode = True

# Properties shared serviceinfo
class ScoreCard(ScoreCardInDBBase):
    id: int
    name: str
    code: str
    update_time:Optional[datetime] = datetime.now() 
    #score: float = 0.0
    #score_value: Optional[float] = None

    class Config:
        orm_mode = True
 

# Properties properties stored in DB
class ScoreCardInDB(ScoreCardInDBBase):
    pass
