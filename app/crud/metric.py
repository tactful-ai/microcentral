
from sqlalchemy.orm import Session

from ..models import Metric
from ..schemas import MetricCreate, MetricUpdate
from .base import CRUDBase


class CRUDMetric(CRUDBase[Metric, MetricCreate, MetricUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDMetric, self).__init__(Metric, db_session)

    def getByCode(self, code: str):
        return self.db_session.query(Metric).filter(Metric.code == code).first()
    
    def getMetricType(self,metricId: int) -> str:
        subquery=self.db_session.query(Metric.type).filter(
        Metric.id == metricId
      ).scalar()
        print(subquery)
        return subquery
       
    def getMetricName(self, metricId:int) -> str:
        subquery = self.db_session.query(Metric.name).filter(Metric.id == metricId).scalar()
        print("metric:", subquery)
        return subquery
 
    #def getMetricNamesByIds(self, metric_ids: list[int]) -> dict[int, str]:
    #  metrics = self.db_session.query(Metric.metricId, Metric.name).filter(Metric.metricId.in_(metric_ids)).all()

    #  return {metric.metricId: metric.name for metric in metrics}
