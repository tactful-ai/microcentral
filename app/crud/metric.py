
from sqlalchemy.orm import Session

from ..models import Metric
from ..schemas import MetricCreate, MetricUpdate
from .base import CRUDBase


class CRUDMetric(CRUDBase[Metric, MetricCreate, MetricUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDMetric, self).__init__(Metric, db_session)

    def getByCode(self, code: str):
        return self.db_session.query(Metric).filter(Metric.code == code).first()

    def get_all_by_ids(self, metric_ids: set):
        metrics = self.db_session.query(Metric).filter(
            Metric.id.in_(metric_ids)).all()
        return metrics

    def getByName(self, name: str):
        return self.db_session.query(Metric).filter(Metric.name == name).first()

