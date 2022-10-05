
from sqlalchemy.orm import Session

from ...core.models import ServiceMetric
from ...core.schemas.serviceMetric import (ServiceMetricCreate,
                                           ServiceMetricUpdate)
from .base import BaseService


class ServiceMetricsService(BaseService[ServiceMetric, ServiceMetricCreate, ServiceMetricUpdate]):
    def __init__(self, db_session: Session):
        super(ServiceMetricsService, self).__init__(ServiceMetric, db_session)

    def getByScorecardId(self, scorecardId: int) -> list[ServiceMetric]:
        return self.db_session.query(ServiceMetric).filter(ServiceMetric.scorecardId == scorecardId).all()

    def getByServiceId(self, serviceId: int) -> list[ServiceMetric]:
        return self.db_session.query(ServiceMetric).filter(ServiceMetric.serviceId == serviceId).all()


