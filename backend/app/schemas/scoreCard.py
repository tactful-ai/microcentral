from typing import Optional

from pydantic import BaseModel


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
    description: str

    class Config:
        orm_mode = True

# Properties to return to client
class ScoreCard(ScoreCardInDBBase):
    pass

# Properties properties stored in DB
class ScoreCardInDB(ScoreCardInDBBase):
    pass
