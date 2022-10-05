from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from ...database import Base


class Microservice(Base):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    code = Column(String(255), nullable=False)
    description = Column(String(255))
    teamId = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)

    def __repr__(self):
        return f"Microservice(id={self.id}, name={self.name}, code={self.code}, description={self.description}, teamId={self.teamId})"
