
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class Team(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    token = Column(String(255), nullable=False)
    microservices = relationship("Microservice", cascade="all, delete-orphan", primaryjoin="Microservice.teamId == Team.id")

    def __repr__(self):
        return f"Team(id={self.id}, name={self.name}, token={self.token})"
