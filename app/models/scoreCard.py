from app.database.base_class import Base
from sqlalchemy import Column, Integer, String


class Scorecard(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    def __repr__(self):
        return f"<Scorecard(name='{self.name}')>"
