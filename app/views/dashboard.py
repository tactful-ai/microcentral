from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import dependencies

from ..crud import (CRUDMicroservice, CRUDServiceMetric,
                             CRUDTeam)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


# dummy data
metric_data = {
    "name": "Build-Time",
    "type": "int",
    "area": ["Marketing", "Delivery"],
    "description": "measuring building time of a cpu service for one our containers, which considered very essintial"
}

@router.get("/", response_class=HTMLResponse)
def index(request: Request, microservices: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud)):
    all_microservices = microservices.list()
    return templates.TemplateResponse("index.html", {"request": request, "all_microservices": all_microservices})


@router.get("/microservice/{id}", response_class=HTMLResponse)
def microservice(request: Request, id: int, microservices: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud), serviceMetricService: CRUDServiceMetric = Depends(dependencies.getServiceMetricsCrud)):
    microservice = microservices.get(id)
    service_metrics = serviceMetricService.getByServiceId(2)
    dates = "-".join([service_metric.timestamp.strftime("%m/%d/%Y, %H:%M:%S")for service_metric in service_metrics])
    values = [service_metric.value for service_metric in service_metrics]
    print(dates)
    return templates.TemplateResponse("microservice.html", {"request": request, "microservice": microservice, "dates": dates, "values": values})


@router.get("/teams", response_class=HTMLResponse)
def teams(request: Request, teamsService: CRUDTeam = Depends(dependencies.getTeamsCrud)):
    teams = teamsService.list()
    return templates.TemplateResponse("teams.html", {"request": request, "teams": teams})


@router.get("/metrics", response_class=HTMLResponse)
def services(request: Request):
    return templates.TemplateResponse("metrics.html", {"request": request})

@router.get("/metrics/create", response_class=HTMLResponse)
def metric(request: Request):
    return templates.TemplateResponse("create-metric.html", {"request": request, "mode": "create", "char_limit": 100})

@router.get("/metrics/edit/{metric_id}", response_class=HTMLResponse)
def metric(request: Request, metric_id: int):
    api_url = f"http://127.0.0.1:8000/api/v1/metrics/{metric_id}"
    
    response = requests.get(api_url)
    metric_data = response.json()

    return templates.TemplateResponse("create-metric.html", {
        "request": request, "mode": "edit", "char_limit": 100, 
        "metric_data": metric_data
    })
