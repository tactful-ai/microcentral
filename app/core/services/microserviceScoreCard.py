
from sqlalchemy.orm import Session

from ...core.models import MicroserviceScoreCard
from ...core.schemas import (MicroserviceScoreCardCreate,
                             MicroserviceScoreCardUpdate)
from .base import BaseService
from .microservice import MicroservicesService


class MicroserviceScoreCardService(BaseService[MicroserviceScoreCard, MicroserviceScoreCardCreate, MicroserviceScoreCardUpdate]):
    def __init__(self, db_session: Session):
        super(MicroserviceScoreCardService, self).__init__(MicroserviceScoreCard, db_session)
        self.microserviceService = MicroservicesService(db_session)

    def getByTeamId(self, teamId: str):
        microservices = self.microserviceService.getByTeamId(teamId)
        return self.db_session.query(MicroserviceScoreCard).filter(MicroserviceScoreCard.microserviceId.in_([microservice.id for microservice in microservices])).all()
