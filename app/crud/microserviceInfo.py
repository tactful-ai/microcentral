import sqlalchemy
from sqlalchemy.orm import Session
from ..models import Microservice
from ..schemas import MicroserviceInfoBase, team, scoreCard, scoreCardMetrics, serviceMetric
from .base import CRUDBase
from typing import List 
from datetime import datetime
from sqlalchemy.sql import func
from app.api.exceptions import ExceptionCustom
from . import CRUDTeam, CRUDMicroserviceScoreCard, CRUDScoreCard, CRUDMicroservice, CRUDScoreCardMetric, CRUDServiceMetric


class CRUDMicroserviceInfo:
    def __init__(self, db_session: Session):
        self.microsService = CRUDMicroservice(db_session)
        self.teamService = CRUDTeam(db_session)
        self.scoreCardService = CRUDMicroserviceScoreCard(db_session)
        self.scoreCard = CRUDScoreCard(db_session)
        self.scoreCardMetric = CRUDScoreCardMetric(db_session)
        self.serviceMetric = CRUDServiceMetric(db_session)

    # Get one with scorecard list and team name
    def getServiceInfo(self, service_id: int) -> MicroserviceInfoBase:
        print(datetime.now())
        microservice = self.microsService.get(service_id)

        if not microservice:
            raise ExceptionCustom(
                f"Microservice with id {service_id} not found")

        scorecardIds = self.scoreCardService.getByServiceId(microservice.id)
        scorecard_ids = [sc_id.scoreCardId for sc_id in scorecardIds]
        scorecards = self.scoreCard.getByScoreCradIds(scorecard_ids)
        
        service_scorecards = []
        for sc in scorecards:
           update_time = self.serviceMetric.get_timestamp(service_id, sc.id)
           calculated_scores = self.serviceMetric.get_calculated_value(service_id, sc.id)
           service_scorecards.append({
             'id': sc.id,
             'name': sc.name,
             'code': sc.code,
             'update_time' : update_time,
            'score_value' : calculated_scores
        })
           
        service = MicroserviceInfoBase(
            id=microservice.id,
            name=microservice.name,
            description=microservice.description,
            code=microservice.code,
            team_name=microservice.team.name,
            scorecards=service_scorecards
)
        return service
