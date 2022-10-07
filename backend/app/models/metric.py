from app.database.base_class import Base
from sqlalchemy import Column, Enum, Integer, String

typeStates = ('integer', 'boolean')

class Metric(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    code = Column(String, unique=True, index=True)
    area = Column(String, nullable=False)
    description = Column(String, nullable=False)
    type = Column(Enum(*typeStates, name="type", create_type=False), nullable=False)

    def __repr__(self):
        return f"{self.name} ({self.area})"
