
from sqlalchemy.orm import Session

from ..models import ScoreCardMetrics
from ..schemas import ScoreCardMetricsCreate, ScoreCardMetricsUpdate
from .base import CRUDBase


class CRUDScoreCardMetric(CRUDBase[ScoreCardMetrics, ScoreCardMetricsCreate, ScoreCardMetricsUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDScoreCardMetric, self).__init__(ScoreCardMetrics, db_session)

    #def getMetricIdByScoreCardId(self, scorecard_id):
    #    # Query to get the metric_id associated with the score_card_id from the ScoreCardMetric table
    #    scorecard_metric = (
    #        self.db_session.query(ScoreCardMetrics)
    #        .filter(ScoreCardMetrics.scoreCardId == scorecard_id)
    #        .first()
    #    )
    #    return scorecard_metric.metricId if scorecard_metric else None
      
    def getMetricByScoreCradId(self, scorecard_id: int) -> list[ScoreCardMetrics]:
        return self.db_session.query(ScoreCardMetrics).filter(ScoreCardMetrics.scoreCardId == scorecard_id).all() 
        