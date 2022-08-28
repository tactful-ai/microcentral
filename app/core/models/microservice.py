from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Microservice(Base):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    description = Column(String(255))
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

    def __repr__(self):
        return f"<Microservice(name='{self.name}')>"
