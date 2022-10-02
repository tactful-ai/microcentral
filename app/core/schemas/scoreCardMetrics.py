from pydantic import BaseModel


class ScoreCardMetrics(BaseModel):
    id: int
    scorecardId: int
    metricId: int

    class Config:
        orm_mode = True

class ScoreCardMetricsCreate(ScoreCardMetrics):
    scorecardId: int
    metricId: int

    class Config:
        orm_mode = True

class ScoreCardMetricsUpdate(ScoreCardMetricsCreate):
    pass
