from sqlalchemy.orm import Session
from ..models import Scorecard
from ..schemas.scoreCard import ScoreCardCreate, ScoreCardUpdate
from .base import CRUDBase
from sqlalchemy import func


class CRUDScoreCard(CRUDBase[Scorecard, ScoreCardCreate, ScoreCardUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDScoreCard, self).__init__(Scorecard, db_session)

    def getByScoreCardId(self, ScoreCardId: str) -> Scorecard:
        return self.db_session.query(Scorecard).filter(Scorecard.id == ScoreCardId).first()

    def getByScoreCardIds(self, ScoreCardIds: list[int]):
        ids =[ScoreCardId for ScoreCardId in ScoreCardIds]
        return self.db_session.query(Scorecard).filter(Scorecard.id.in_(ids)).all()
    
    def getByScoreCardCode(self, code: str):
        return self.db_session.query(Scorecard).filter(Scorecard.code == code).all()