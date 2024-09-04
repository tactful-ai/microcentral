from typing import Optional, Union

from pydantic import BaseModel


# Shared properties
class ScoreCardMetricsBase(BaseModel):
    scoreCardId: Optional[int] = None
    metricId: Optional[int] = None
    
    criteria: Optional[str] = None
    desiredValue: Optional[Union[str,float,int,str]] = None
    weight: Optional[int] = None
    
# class ScoreCardMetricsGet(ScoreCardMetricsBase):

# Properties to receive on ScoreCardMetrics creation
class ScoreCardMetricsCreate(ScoreCardMetricsBase):
    scoreCardId: int
    metricId: int 
    criteria: str
    desiredValue: Optional[Union[str,float,int,str]] = None
    weight: int
    
    
# Properties to receive on ScoreCardMetrics update
class ScoreCardMetricsUpdate(ScoreCardMetricsBase):
    pass

# Properties shared by models stored in DB
class ScoreCardMetricsInDBBase(ScoreCardMetricsBase):
    id: int
    scoreCardId: int
    metricId: int
    
    criteria: str
    desiredValue: Optional[Union[str,float,int,str]] = None
    weight: int
    

    class Config:
        orm_mode = True

# Properties to return to client
class ScoreCardMetrics(ScoreCardMetricsInDBBase):
    pass

# Properties properties stored in DB
class ScoreCardMetricsInDB(ScoreCardMetricsInDBBase):
    pass
