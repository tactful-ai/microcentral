from app.database.base_class import Base
from sqlalchemy import Column, Integer, String

# change
class Scorecard(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    def __repr__(self):
        return f"<Scorecard(name='{self.name}')>"
