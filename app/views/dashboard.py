import datetime

from app.core.services import MicroservicesService, get_service
from app.core.services.serviceMetric import ServiceMetricsService
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request, microservices: MicroservicesService = Depends(get_service('microservices'))):
    all_microservices = microservices.list()
    return templates.TemplateResponse("index.html", {"request": request, "all_microservices": all_microservices})


@router.get("/microservice/{id}", response_class=HTMLResponse)
def microservice(request: Request, id: int, microservices: MicroservicesService = Depends(get_service('microservices')), serviceMetricService: ServiceMetricsService = Depends(get_service('serviceMetrics'))):
    microservice = microservices.get(id)
    service_metrics = serviceMetricService.getByScorecardId(2)
    dates = "-".join([service_metric.timestamp.strftime("%m/%d/%Y, %H:%M:%S")for service_metric in service_metrics])
    values = [service_metric.value for service_metric in service_metrics]
    print(dates)
    return templates.TemplateResponse("microservice.html", {"request": request, "microservice": microservice, "dates": dates, "values": values})
