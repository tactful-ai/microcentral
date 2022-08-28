
from app.core.models import Scorecard
from app.core.schemas.scorecard import ScorecardCreate, ScorecardUpdate
from sqlalchemy.orm import Session

from .base import BaseService


class ScorecardsService(BaseService[Scorecard, ScorecardCreate, ScorecardUpdate]):
    def __init__(self, db_session: Session):
        super(ScorecardsService, self).__init__(Scorecard, db_session)

