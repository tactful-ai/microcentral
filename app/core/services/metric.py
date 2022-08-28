
from app.core.models import Metric
from app.core.schemas.metric import MetricCreate, MetricUpdate
from sqlalchemy.orm import Session

from .base import BaseService


class MetricsService(BaseService[Metric, MetricCreate, MetricUpdate]):
    def __init__(self, db_session: Session):
        super(MetricsService, self).__init__(Metric, db_session)

