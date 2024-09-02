
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
        subquery = self.scorecardMetrics.getMetricByScoreCradId(scorecard_id)

        update_time = self.db_session.query(ServiceMetric.timestamp)\
            .filter(ServiceMetric.serviceId == service_id, ServiceMetric.metricId.in_(subquery))\
            .order_by(ServiceMetric.timestamp.desc())\
            .first()

        if update_time:
          formatted_time = update_time.timestamp.strftime('%Y-%m-%d %H:%M:%S')
          return formatted_time
        else:
         return None 