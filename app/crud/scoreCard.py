
from sqlalchemy.orm import Session

from ..models import Scorecard
from ..schemas.scoreCard import ScoreCardCreate, ScoreCardUpdate
from .base import CRUDBase


class CRUDScoreCard(CRUDBase[Scorecard, ScoreCardCreate, ScoreCardUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDScoreCard, self).__init__(Scorecard, db_session)

    def getByScoreCradId(self, ScoreCardId: str):
        return self.db_session.query(Scorecard).filter(Scorecard.id == ScoreCardId).all()

