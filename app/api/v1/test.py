from app.core.services import ServiceMetricsService, get_service
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/testApi/")
def testGet(service_metrics:ServiceMetricsService = Depends(get_service('serviceMetrics'))):
    return service_metrics.list()
