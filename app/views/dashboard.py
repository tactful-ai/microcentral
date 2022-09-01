from app.core.services import MicroservicesService, get_service
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
def microservice(request: Request, id: int, microservices: MicroservicesService = Depends(get_service('microservices'))):
    microservice = microservices.get(id)
    return templates.TemplateResponse("microservice.html", {"request": request, "microservice": microservice})
