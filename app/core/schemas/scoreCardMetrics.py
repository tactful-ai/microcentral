from pydantic import BaseModel


class ScoreCardMetrics(BaseModel):
    id: int
    scorecardId: int
    metricId: int

    class Config:
        orm_mode = True

class ScoreCardMetricsCreate(BaseModel):
    scorecardId: int
    metricId: int

    class Config:
        orm_mode = True

class ScoreCardMetricsUpdate(ScoreCardMetricsCreate):
    pass
