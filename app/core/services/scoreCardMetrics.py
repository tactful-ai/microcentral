
from app.core.models import ScoreCardMetrics
from app.core.schemas.scoreCardMetrics import (ScoreCardMetricsCreate,
                                               ScoreCardMetricsUpdate)
from sqlalchemy.orm import Session

from .base import BaseService


class ScoreCardMetricsService(BaseService[ScoreCardMetrics, ScoreCardMetricsCreate, ScoreCardMetricsUpdate]):
    def __init__(self, db_session: Session):
        super(ScoreCardMetricsService, self).__init__(ScoreCardMetrics, db_session)

