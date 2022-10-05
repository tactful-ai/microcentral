from app.core.schemas import ServiceMetricCreate
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from ..core.services import (JWTBearer, MetricsService,
                             MicroserviceScoreCardService,
                             MicroservicesService, ServiceMetricsService,
                             decodeJWT, get_service)


class Value(BaseModel):
    value: int | bool | float | str = Field(..., title="Value", description="Value of the metric")

router = APIRouter()


@router.post("/{service_code}/{metric_code}")
def create(service_code: str, metric_code: str, value: Value,
    metricsService: MetricsService = Depends(get_service('metrics')),
    microservicesService: MicroservicesService = Depends(get_service('microservices')),
    serviceMetricsService: ServiceMetricsService = Depends(get_service('serviceMetrics')),
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
def get_all_metrics(serviceMetricsService: ServiceMetricsService = Depends(get_service('serviceMetrics'))):

    return serviceMetricsService.list()

@router.get("/allScorecards")
def getScoreCards(
    microserviceScoreCardService: MicroserviceScoreCardService = Depends(get_service('microserviceScorecards')),
    token = Depends(JWTBearer())
    ):

    teamId = decodeJWT(token)["teamId"]

    return microserviceScoreCardService.getByTeamId(teamId)
