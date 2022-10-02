from sqlalchemy import Column, ForeignKey, Integer, String

from ...database import Base


class Microservice(Base):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    description = Column(String(255))
    teamId = Column(Integer, ForeignKey("teams.id"), nullable=False)

    def __repr__(self):
        return f"<Microservice(name='{self.name}')>"
