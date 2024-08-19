from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import dependencies

from ..crud import (CRUDMicroservice, CRUDServiceMetric,
                             CRUDTeam)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

scorecard_data = {
    "name": "Performance",
    "services": ["Visa Auth", "Google maps"],
    "description": "measuring the performance of the service according to standard metrics.",
    "metrics": [
        {
            "name": "build-time",
            "criteria": "less-than",
            "number": 3 ,
            "weight": 30
        },
        {
            "name": "cpu-usage",
            "criteria": "equal",
            "number": 1000 ,
            "weight": 70
        }
    ]
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

@router.get('/scorecards/create', response_class=HTMLResponse)
def metrics(request: Request):
    return templates.TemplateResponse("create-scorecard.html", {"request": request, "mode": "create", "char_limit": 100})

@router.get('/scorecards/edit/{scorecard_id}', response_class=HTMLResponse)
def metrics(request: Request, scorecard_id: int):
    return templates.TemplateResponse("create-scorecard.html", {
        "request": request, 
        "mode": "edit",
        "char_limit": 100,
        "scorecard_data": scorecard_data
    })