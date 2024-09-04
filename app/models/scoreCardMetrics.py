from app.database.base_class import Base
from sqlalchemy import Column, Integer, Enum, String

criteriaStates = ("greater", "smaller", "equal", "greater or equal", "smaller or equal")

class ScoreCardMetrics(Base):
    id = Column(Integer, primary_key=True, index=True)
    scoreCardId = Column(Integer, nullable=False)
    metricId = Column(Integer, nullable=False)
    
    criteria = Column(Enum(*criteriaStates, name="criteria", create_type=False), nullable=False)
    desiredValue = Column(String, nullable=False)
    weight = Column(Integer, nullable=False)
    

    def __repr__(self):
        return f"<ScoreCardMetrics(id='{self.id}', scoreCardId='{self.scoreCardId}', metricId='{self.metricId}')>"
    