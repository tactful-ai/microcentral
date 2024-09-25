from typing import Any
from sqlalchemy.orm import Session
from ..models import MicroserviceScoreCard , Scorecard
from ..schemas import MicroserviceScoreCardCreate, MicroserviceScoreCardUpdate
from .base import CRUDBase
from .microservice import CRUDMicroservice


class CRUDMicroserviceScoreCard(CRUDBase[MicroserviceScoreCard, MicroserviceScoreCardCreate, MicroserviceScoreCardUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDMicroserviceScoreCard, self).__init__(MicroserviceScoreCard, db_session)
        self.microserviceService = CRUDMicroservice(db_session)

    def getByTeamId(self, teamId: str):
        microservices = self.microserviceService.getByTeamId(teamId)
        return self.db_session.query(MicroserviceScoreCard).filter(MicroserviceScoreCard.microserviceId.in_([microservice.id for microservice in microservices])).all()

    def getByServiceId(self, serviceId: int) -> list[MicroserviceScoreCard]:
        return self.db_session.query(MicroserviceScoreCard).filter(MicroserviceScoreCard.microserviceId == serviceId).all()

    def deleteByServiceId(self,serviceid:int):
        self.db_session.query(MicroserviceScoreCard).filter(MicroserviceScoreCard.microserviceId == serviceid).delete()
        self.db_session.commit()

    def getservice(self, scorecardId: int) -> MicroserviceScoreCard:
        return self.db_session.query(MicroserviceScoreCard).filter(MicroserviceScoreCard.scoreCardId == scorecardId).all()
    
    def deleteByScorecardId(self, scorecardID:int):
        self.db_session.query(MicroserviceScoreCard).filter(MicroserviceScoreCard.scoreCardId == scorecardID).delete()
        self.db_session.commit()
        
    def get_scorecard_names_by_service_id(self, service_id: int) -> list[str]:
        scorecard_names = (
            self.db_session.query(Scorecard.name)
            .join(MicroserviceScoreCard, Scorecard.id == MicroserviceScoreCard.scorecardId)
            .filter(MicroserviceScoreCard.serviceId == service_id)
            .all()
        )
       
        return [name for (name,) in scorecard_names]    