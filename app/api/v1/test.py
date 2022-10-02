from fastapi import APIRouter, Depends

from ...core.services import ServiceMetricsService, get_service

router = APIRouter()


@router.get("/testApi/")
def testGet(service_metrics:ServiceMetricsService = Depends(get_service('serviceMetrics'))):
    return service_metrics.list()
