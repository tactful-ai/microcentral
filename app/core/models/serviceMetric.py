from datetime import datetime

from app.database import Base
from sqlalchemy import Column, DateTime, Integer


class ServiceMetric(Base):
    id = Column(Integer, primary_key=True, index=True)

    ServiceId = Column(Integer, nullable=False)
    metricId = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<ServiceMetric(id='{self.id}', ServiceId='{self.ServiceId}', metricId='{self.metricId}', value='{self.value}', timestamp='{self.timestamp}')>"

# Sperate the value from the relation
# ScoreCardMetrics: scorecard_id, metric_id
