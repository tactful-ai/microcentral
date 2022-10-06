
from sqlalchemy.orm import Session

from ..models import Scorecard
from ..schemas.scorecard import ScorecardCreate, ScorecardUpdate
from .base import CRUDBase


class CRUDScorecard(CRUDBase[Scorecard, ScorecardCreate, ScorecardUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDScorecard, self).__init__(Scorecard, db_session)

