from datetime import datetime

from app.database.base_class import Base
from sqlalchemy import Column, DateTime, Integer


class ServiceMetric(Base):
    id = Column(Integer, primary_key=True, index=True)
    serviceId = Column(Integer, nullable=False)
    metricId = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<ServiceMetric(id='{self.id}', ServiceId='{self.serviceId}', metricId='{self.metricId}', value='{self.value}', timestamp='{self.timestamp}')>"
