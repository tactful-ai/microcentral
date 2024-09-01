
from sqlalchemy.orm import Session

from ..models import ServiceMetric, scoreCardMetrics
from ..schemas import ServiceMetricCreate, ServiceMetricUpdate
from .base import CRUDBase
from . import CRUDScoreCardMetric


class CRUDServiceMetric(CRUDBase[ServiceMetric, ServiceMetricCreate, ServiceMetricUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDServiceMetric, self).__init__(ServiceMetric, db_session)
        self.scorecardMetrics = CRUDScoreCardMetric(db_session)

    def getByScorecardId(self, scorecardId: int) -> list[ServiceMetric]:
        return self.db_session.query(ServiceMetric).filter(ServiceMetric.scorecardId == scorecardId).all()

    def getByServiceId(self, serviceId: int) -> list[ServiceMetric]:
        return self.db_session.query(ServiceMetric).filter(ServiceMetric.serviceId == serviceId).all()

    def get_timestamp(self, service_id: int, scorecard_id: int):
        metric_ids = self.scorecardMetrics.getMetricByScoreCradId(scorecard_id)
        metric_ids = [metric_id[0]
                      for metric_id in metric_ids] 

        if not metric_ids:
            return None 

        update_time = self.db_session.query(ServiceMetric.timestamp)\
                .filter(ServiceMetric.serviceId == service_id, ServiceMetric.metricId.in_(metric_ids))\
                .order_by(ServiceMetric.timestamp.desc())\
                .first()

        return update_time[0] if update_time else None
