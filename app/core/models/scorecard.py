from sqlalchemy import Column, Integer, String

from ...database import Base


class Scorecard(Base):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    microserviceId = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Scorecard(name='{self.name}')>"
