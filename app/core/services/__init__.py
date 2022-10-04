from fastapi import Depends
from sqlalchemy.orm import Session

from ...database import get_session
from .authentication import *
from .base import BaseService
from .metric import MetricsService
from .microservice import MicroservicesService
from .scorecard import ScorecardsService
from .scoreCardMetrics import ScoreCardMetricsService
from .serviceMetric import ServiceMetricsService
from .team import TeamsService


def _get_metrics_service(db_session: Session = Depends(get_session)) -> MetricsService:
    return MetricsService(db_session)

def _get_microservices_service(db_session: Session = Depends(get_session)) -> MicroservicesService:
    return MicroservicesService(db_session)

def _get_scorecards_service(db_session: Session = Depends(get_session)) -> ScorecardsService:
    return ScorecardsService(db_session)

def _get_service_metrics_service(db_session: Session = Depends(get_session)) -> ServiceMetricsService:
    return ServiceMetricsService(db_session)

def _get_teams_service(db_session: Session = Depends(get_session)) -> TeamsService:
    return TeamsService(db_session)

def _get_scorecard_metrics_service(db_session: Session = Depends(get_session)) -> ScoreCardMetricsService:
    return ScoreCardMetricsService(db_session)



def get_services() -> dict:
    return {
        'metrics': _get_metrics_service,
        'teams': _get_teams_service,
        'microservices': _get_microservices_service,
        'scorecards': _get_scorecards_service,
        'serviceMetrics': _get_service_metrics_service,
        'scorecardMetrics': _get_scorecard_metrics_service,
    }


def get_service(service_name: str) -> BaseService:
    return get_services()[service_name]
