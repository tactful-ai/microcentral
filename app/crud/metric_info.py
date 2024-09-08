from ..schemas import team, scoreCard, scoreCardMetrics, serviceMetric
from .base import CRUDBase
import sqlalchemy
from sqlalchemy.orm import Session
from . import CRUDTeam, CRUDMicroserviceScoreCard, CRUDScoreCard, CRUDMicroservice, CRUDScoreCardMetric, CRUDServiceMetric


class CRUDMetricInfo:
    def __init__(self, db_session: Session):
              self.serviceMetric = CRUDServiceMetric(db_session)