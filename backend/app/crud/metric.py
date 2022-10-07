
from sqlalchemy.orm import Session

from ..models import Metric
from ..schemas import MetricCreate, MetricUpdate
from .base import CRUDBase


class CRUDMetric(CRUDBase[Metric, MetricCreate, MetricUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDMetric, self).__init__(Metric, db_session)

    def getByCode(self, code: str):
        return self.db_session.query(Metric).filter(Metric.code == code).first()

