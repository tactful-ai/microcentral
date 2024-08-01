
from sqlalchemy.orm import Session

from ...core.models import ScoreCardMetrics
from ...core.schemas.scoreCardMetrics import (ScoreCardMetricsCreate,
                                              ScoreCardMetricsUpdate)
from .base import BaseService


class ScoreCardMetricsService(BaseService[ScoreCardMetrics, ScoreCardMetricsCreate, ScoreCardMetricsUpdate]):
    def __init__(self, db_session: Session):
        super(ScoreCardMetricsService, self).__init__(ScoreCardMetrics, db_session)

