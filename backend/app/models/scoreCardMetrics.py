from app.database.base_class import Base
from sqlalchemy import Column, Integer


class ScoreCardMetrics(Base):
    id = Column(Integer, primary_key=True, index=True)
    scoreCardId = Column(Integer, nullable=False)
    metricId = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<ScoreCardMetrics(id='{self.id}', scoreCardId='{self.scoreCardId}', metricId='{self.metricId}')>"
