
from app.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Team(Base):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    microservices = relationship("Microservice", cascade="all, delete-orphan", primaryjoin="Microservice.team_id == Team.id")

    def __repr__(self):
        return f"<Team(name='{self.name}')>"
