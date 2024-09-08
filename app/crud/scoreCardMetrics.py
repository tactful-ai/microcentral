
from sqlalchemy.orm import Session

from ..models import ScoreCardMetrics
from ..schemas import ScoreCardMetricsCreate, ScoreCardMetricsUpdate
from .base import CRUDBase


class CRUDScoreCardMetric(CRUDBase[ScoreCardMetrics, ScoreCardMetricsCreate, ScoreCardMetricsUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDScoreCardMetric, self).__init__(ScoreCardMetrics, db_session)
    
    def getbyscorecardID(self, scorecardID) -> list[ScoreCardMetrics]:
        return self.db_session.query(ScoreCardMetrics).filter(ScoreCardMetrics.scoreCardId == scorecardID).all()

    def getbymetricID(self, metricID) :
        return self.db_session.query(ScoreCardMetrics).filter(ScoreCardMetrics.metricId == metricID).first()