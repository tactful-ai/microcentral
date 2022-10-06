from app.database.base_class import Base
from sqlalchemy import Column, Integer


class MicroserviceScoreCard(Base):
    id = Column(Integer, primary_key=True, index=True)
    microserviceId = Column(Integer, nullable=False)
    scorecardId = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<MicroserviceScoreCard(id='{self.id}', microserviceId='{self.microserviceId}', scorecardId='{self.scorecardId}')>"
