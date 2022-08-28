
from app.core.models import ServiceMetric
from app.core.schemas.serviceMetric import (ServiceMetricCreate,
                                            ServiceMetricUpdate)
from sqlalchemy.orm import Session

from .base import BaseService


class ServiceMetricsService(BaseService[ServiceMetric, ServiceMetricCreate, ServiceMetricUpdate]):
    def __init__(self, db_session: Session):
        super(ServiceMetricsService, self).__init__(ServiceMetric, db_session)

