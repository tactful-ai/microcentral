from typing import Optional

from pydantic import BaseModel


# Shared properties
class ScoreCardMetricsBase(BaseModel):
    scoreCardId: Optional[int] = None
    metricId: Optional[int] = None

# Properties to receive on ScoreCardMetrics creation
class ScoreCardMetricsCreate(ScoreCardMetricsBase):
    scoreCardId: int
    metricId: int

# Properties to receive on ScoreCardMetrics update
class ScoreCardMetricsUpdate(ScoreCardMetricsBase):
    pass

# Properties shared by models stored in DB
class ScoreCardMetricsInDBBase(ScoreCardMetricsBase):
    id: int
    scoreCardId: int
    metricId: int

    class Config:
        orm_mode = True

# Properties to return to client
class ScoreCardMetrics(ScoreCardMetricsInDBBase):
    pass

# Properties properties stored in DB
class ScoreCardMetricsInDB(ScoreCardMetricsInDBBase):
    pass
