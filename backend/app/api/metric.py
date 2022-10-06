from app.core.authentication import JWTBearer, decodeJWT
from app.schemas import ServiceMetricCreate
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from ..crud import (CRUDMetric, CRUDMicroservice, CRUDMicroserviceScoreCard,
                    CRUDServiceMetric, get_metrics_service,
                    get_microservice_score_card_service,
                    get_microservices_service, get_service_metrics_service)


class Value(BaseModel):
    value: int | bool | float | str = Field(..., title="Value", description="Value of the metric")

router = APIRouter()


@router.post("/{service_code}/{metric_code}")
def create(service_code: str, metric_code: str, value: Value,
    metricsService: CRUDMetric = Depends(get_metrics_service),
    microservicesService: CRUDMicroservice = Depends(get_microservices_service),
    serviceMetricsService: CRUDServiceMetric = Depends(get_service_metrics_service),
    token = Depends(JWTBearer())
    ):
    service_code = service_code.replace(" ", "-").lower()
    metric_code = metric_code.replace(" ", "-").lower()

    teamId = decodeJWT(token)["teamId"]

    service = microservicesService.getByTeamIdAndCode(teamId, service_code)
    if service is None:
        return {"error": "Service not found"}

    metric = metricsService.getByCode(metric_code)
    if metric is None:
        return {"error": "Metric not found"}

    serviceMetricsService.create(ServiceMetricCreate(serviceId=service.id, metricId=metric.id, value=value.value))

    return {"message": "Metric created"}


@router.get("/allMetrics")
def get_all_metrics(serviceMetricsService: CRUDServiceMetric = Depends(get_service_metrics_service)):

    return serviceMetricsService.list()

@router.get("/allScorecards")
def getScoreCards(
    microserviceScoreCardService: CRUDMicroserviceScoreCard = Depends(get_microservice_score_card_service),
    token = Depends(JWTBearer())
    ):

    teamId = decodeJWT(token)["teamId"]

    return microserviceScoreCardService.getByTeamId(teamId)
