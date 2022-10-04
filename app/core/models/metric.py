from sqlalchemy import Column, Enum, Integer, String

from ...database import Base

typeStates = ('integer', 'boolean')

class Metric(Base):
    id = Column(Integer, primary_key=True, index=True)

    area = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    type = Column(Enum(*typeStates, name="type", create_type=False), nullable=False)

    def __repr__(self):
        return f"<Metric(area='{self.area}', description='{self.description}', type='{self.type}')>"

