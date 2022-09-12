from datetime import datetime

from app.database import Base
from sqlalchemy import Column, DateTime, Integer


class ServiceMetric(Base):
    id = Column(Integer, primary_key=True, index=True)

    scorecard_id = Column(Integer, nullable=False)
    metric_id = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<ServiceMetric(name='{self.value}')>"
