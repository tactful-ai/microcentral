from sqlalchemy.orm import Session
from app.api.exceptions import HTTPResponseCustomized

from ..models import Scorecard
from ..schemas import scorecardServiceMetricCreate
from . import CRUDScoreCardMetric, CRUDMicroserviceScoreCard, CRUDMetric, CRUDScoreCard, CRUDMicroservice
from .base import CRUDBase
from app.utils import format_code
from fastapi.encoders import jsonable_encoder

class CRUDScoreCardServiceMetric:
  def __init__(self, db_session: Session):
    self.scoreCard = CRUDScoreCard(db_session)
    self.microServiceScoreCard = CRUDMicroserviceScoreCard(db_session)
    self.scoreCardMetric = CRUDScoreCardMetric(db_session)
    self.microService = CRUDMicroservice(db_session)

  def getwithscorecardIDmetricandservice(self, scorecardID:int):
    # it handles if the scorecard is not found & raises error message
    scorecard = self.scoreCard.get(scorecardID)

    metricIDs = self.scoreCardMetric.getbyscorecardID(scorecardID)
    serviceIDs = self.microServiceScoreCard.getservice(scorecardID)

    metricOBJs = []
    serviceOBJs = []
    metric_ids = [sc_id.metricId for sc_id in metricIDs]
    service_ids = [sc_id.microserviceId for sc_id in serviceIDs]

    print (metric_ids)
    print (service_ids)

    
    for metricID in metric_ids:
      metric = self.scoreCardMetric.getbymetricID(metricID)
      metricOBJs.append({
        'scoreCardId': metric.scoreCardId,
        'metricId': metric.metricId,
        'criteria': metric.criteria,
        'desiredValue': metric.desiredValue,
        'weight': metric.weight
      })

    print(metricOBJs)

    for serviceID in service_ids:
      service = self.microService.getByServiceId(serviceID)
      print (service)
      serviceOBJs.append({
        'name': service.name,
        'description': service.description,
        'code': service.code,
        'teamId': service.teamId
      })

    print(serviceOBJs)
    
    scorecard.code = format_code(scorecard.name)
    print (scorecard.name)
    scorecard = scorecardServiceMetricCreate(
      name = scorecard.name,
      code = scorecard.code,
      description = scorecard.description,
      metrics = metricOBJs,
      services = serviceOBJs
    )

    return metricIDs