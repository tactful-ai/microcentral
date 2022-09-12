from app.database import Base
from sqlalchemy import Column, Integer, String


class Scorecard(Base):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    microservice_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Scorecard(name='{self.name}')>"