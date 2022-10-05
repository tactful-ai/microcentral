from sqlalchemy import Column, Integer

from ...database import Base


class ScoreCardMetrics(Base):
    id = Column(Integer, primary_key=True, index=True)
    scorecardId = Column(Integer, nullable=False)
    metricId = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<ScoreCardMetrics(id='{self.id}', scorecardId='{self.scorecardId}', metricId='{self.metricId}')>"
