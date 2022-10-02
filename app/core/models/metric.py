from sqlalchemy import Column, Integer, String

from ...database import Base


class Metric(Base):
    id = Column(Integer, primary_key=True, index=True)

    area = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    type = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Metric(area='{self.area}', description='{self.description}', type='{self.type}')>"

