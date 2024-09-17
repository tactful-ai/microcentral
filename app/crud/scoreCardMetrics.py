
from sqlalchemy.orm import Session

from ..models import ScoreCardMetrics
from ..schemas import ScoreCardMetricsCreate, ScoreCardMetricsUpdate
from .base import CRUDBase


class CRUDScoreCardMetric(CRUDBase[ScoreCardMetrics, ScoreCardMetricsCreate, ScoreCardMetricsUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDScoreCardMetric, self).__init__(ScoreCardMetrics, db_session)

    def getMetricByScoreCradId(self, scorecard_id: int):
        return self.db_session.query(ScoreCardMetrics.metricId).filter(ScoreCardMetrics.scoreCardId == scorecard_id).subquery()

    def getMetricWeight(self, scorecard_id: int) -> list[ScoreCardMetrics]:
        return self.db_session.query(ScoreCardMetrics.metricId, ScoreCardMetrics.weight)\
            .filter(ScoreCardMetrics.scoreCardId == scorecard_id)\
            .all()

    def get_metrics(self, scorecard_id: int) -> list[ScoreCardMetrics]:
        metrics = self.db_session.query(

            ScoreCardMetrics.metricId,
            ScoreCardMetrics.criteria,
            ScoreCardMetrics.desiredValue,
            ScoreCardMetrics.weight
        ).filter(
            ScoreCardMetrics.scoreCardId == scorecard_id
        ).all()

        return metrics
