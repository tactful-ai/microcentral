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

    
    def getbyscorecardID(self, scorecardID: int) -> ScoreCardMetrics:
        return self.db_session.query(ScoreCardMetrics).filter(ScoreCardMetrics.scoreCardId == scorecardID).all()

    def getbymetricIDandScorecardID(self, metricID: int, scorecardID: int):
        return (
            self.db_session.query(ScoreCardMetrics)
            .filter(ScoreCardMetrics.metricId == metricID, ScoreCardMetrics.scoreCardId == scorecardID)
            .first()
        )
    
    def getByMetricIdsandScorecardId(self , metricIds: list[int], scorecardId: int):
        return (self.db_session.query(ScoreCardMetrics)
                .filter(ScoreCardMetrics.metricId.in_(metricIds), 
                        ScoreCardMetrics.scoreCardId == scorecardId)).all()

    
    def deleteByScorecardId(self, scorecardID:int):
        self.db_session.query(ScoreCardMetrics).filter(ScoreCardMetrics.scoreCardId == scorecardID).delete()
        self.db_session.commit()

    def getIdByScorecardID(self, scorecardID: int) -> list[int]:
        return self.db_session.query(ScoreCardMetrics.id).filter(ScoreCardMetrics.scoreCardId == scorecardID).all()