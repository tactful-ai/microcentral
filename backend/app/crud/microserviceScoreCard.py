
from sqlalchemy.orm import Session

from ..models import MicroserviceScoreCard
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
