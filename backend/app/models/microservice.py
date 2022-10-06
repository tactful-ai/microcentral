from app.database.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class Microservice(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    description = Column(String)
    teamId = Column(UUID(as_uuid=True), ForeignKey("team.id"), nullable=False)

    def __repr__(self):
        return f"Microservice(id={self.id}, name={self.name}, code={self.code}, description={self.description}, teamId={self.teamId})"
