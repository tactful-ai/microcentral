
from sqlalchemy.orm import Session

from ..models import ScoreCardMetrics
from ..schemas import ScoreCardMetricsCreate, ScoreCardMetricsUpdate
from .base import CRUDBase


class CRUDScoreCardMetric(CRUDBase[ScoreCardMetrics, ScoreCardMetricsCreate, ScoreCardMetricsUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDScoreCardMetric, self).__init__(ScoreCardMetrics, db_session)

    def getMetricByScoreCradId(self, scorecard_id: int) :
        return self.db_session.query(ScoreCardMetrics.metricId).filter(ScoreCardMetrics.scoreCardId == scorecard_id).subquery() 
        
      