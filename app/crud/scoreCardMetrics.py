
from sqlalchemy.orm import Session

from ..models import ScoreCardMetrics
from ..schemas import ScoreCardMetricsCreate, ScoreCardMetricsUpdate
from .base import CRUDBase


class CRUDScoreCardMetric(CRUDBase[ScoreCardMetrics, ScoreCardMetricsCreate, ScoreCardMetricsUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDScoreCardMetric, self).__init__(ScoreCardMetrics, db_session)
    
    def getbyscorecardID(self, scorecardID: list[int]) -> list[ScoreCardMetrics]:
        return self.db_session.query(ScoreCardMetrics).filter(ScoreCardMetrics.scoreCardId.in_(scorecardID)).all()
        #return self.db_session.query(ScoreCardMetrics).filter(ScoreCardMetrics.scoreCardId == scorecardID).all()

    def getbymetricID(self, metricID: int) -> ScoreCardMetrics :
        return self.db_session.query(ScoreCardMetrics).filter(ScoreCardMetrics.metricId == metricID).first()
    
    def getbymetricIDandScorecardID(self, metricID: int, scorecardID: int):
        return (
            self.db_session.query(ScoreCardMetrics)
            .filter(ScoreCardMetrics.metricId == metricID, ScoreCardMetrics.scoreCardId == scorecardID)
            .first()
        )
    
    def deleteByScorecardId(self, scorecardID:int):
        self.db_session.query(ScoreCardMetrics).filter(ScoreCardMetrics.scoreCardId == scorecardID).delete()
        self.db_session.commit()