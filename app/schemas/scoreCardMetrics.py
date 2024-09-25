from typing import Optional, Union
from typing import Optional, Union

from pydantic import BaseModel


# Shared properties
class ScoreCardMetricsBase(BaseModel):
    scoreCardId: Optional[int] = None
    metricId: Optional[int] = None
    criteria: Optional[str] = None
    desiredValue: Optional[Union[str, float, int, bool]] = None
    weight: Optional[int] = None


# Properties to receive on ScoreCardMetrics creation
class ScoreCardMetricsCreate(ScoreCardMetricsBase):
    scoreCardId: int
    criteria: str
    desiredValue: Union[str, float, int, bool]
    weight: int

# Properties to receive on ScoreCardMetrics update


# Properties shared by models stored in DB
class ScoreCardMetricsInDBBase(ScoreCardMetricsBase):
    id: int
    scoreCardId: int
    metricId: int

    criteria: str
    desiredValue: Optional[Union[str, float, int, bool]] = None
    weight: int

    class Config:
        orm_mode = True

class ScoreCardMetricsUpdate(ScoreCardMetricsInDBBase):
    pass


class MetricListforScorecardGet(BaseModel):
    id: int  # This one is metricID
    criteria: str
    desiredValue: Optional[Union[str, float, int, bool]] = None
    weight: int


# Properties to return to client
class ScoreCardMetrics(ScoreCardMetricsInDBBase):
    pass

# Properties properties stored in DB


class ScoreCardMetricsInDB(ScoreCardMetricsInDBBase):
    pass


class MetricCreateScorecard(BaseModel):
    criteria: str
    desiredValue: Union[str, float, int, bool]
    weight: int
    id: int


class MetricTypeScorecard(MetricCreateScorecard):
    type: str
