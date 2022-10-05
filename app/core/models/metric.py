from sqlalchemy import Column, Enum, Integer, String

from ...database import Base

typeStates = ('integer', 'boolean')

class Metric(Base):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), unique=True, index=True)
    code = Column(String(255), unique=True, index=True)
    area = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    type = Column(Enum(*typeStates, name="type", create_type=False), nullable=False)

    def __repr__(self):
        return f"{self.name} ({self.area})"

