from .base import CRUDBase
from .metric import CRUDMetric
from .microservice import CRUDMicroservice
from .microserviceScoreCard import CRUDMicroserviceScoreCard
from .scoreCard import CRUDScoreCard
from .scoreCardMetrics import CRUDScoreCardMetric
from .serviceMetric import CRUDServiceMetric
from .team import CRUDTeam


def get_metrics_service(db_session):
    return CRUDMetric(db_session)

def get_microservices_service(db_session):
    return CRUDMicroservice(db_session)

def get_microservice_score_card_service(db_session):
    return CRUDMicroserviceScoreCard(db_session)

def get_score_card_service(db_session):
    return CRUDScoreCard(db_session)

def get_score_card_metrics_service(db_session):
    return CRUDScoreCardMetric(db_session)

def get_service_metrics_service(db_session):
    return CRUDServiceMetric(db_session)

def get_teams_service(db_session):
    return CRUDTeam(db_session)
