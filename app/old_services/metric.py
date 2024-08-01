
from sqlalchemy.orm import Session

from ..models import Metric
from ..schemas.metric import MetricCreate, MetricUpdate
from .base import BaseService


class MetricsService(BaseService[Metric, MetricCreate, MetricUpdate]):
    def __init__(self, db_session: Session):
        super(MetricsService, self).__init__(Metric, db_session)

    def getByCode(self, code: str):
        return self.db_session.query(Metric).filter(Metric.code == code).first()

