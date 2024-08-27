from fastapi.exceptions import RequestValidationError
from app.schemas import ServiceMetricCreate, MetricCreate
from fastapi import APIRouter, Depends, Request, exception_handlers, status, Response, HTTPException, FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from app.crud import CRUDMetric, CRUDServiceMetric, CRUDMicroserviceScoreCard, CRUDMicroservice
from app import schemas, models, crud
from typing import Any, Callable
import json
import re
from fastapi.routing import APIRoute
from .exceptions import ExceptionCustom



from app import dependencies 
from app.core.security import JWTBearer, decodeJWT

class Value(BaseModel):
    value: int | bool | float | str = Field(..., title="Value", description="Value of the metric")

router = APIRouter()
app = FastAPI()

def format_code(name):
    code = re.sub(r'\s+', '-', name.strip())
    return code

"""
# OLD ONES NOT USED ANYMORE
@router.post("/{service_code}/{metric_code}")
def create(service_code: str, metric_code: str, value: Value,
    metricsService: CRUDMetric = Depends(dependencies.getMetricsCrud),
    microservicesService: CRUDMicroservice = Depends(dependencies.getMicroservicesCrud),
    serviceMetricsService: CRUDServiceMetric = Depends(dependencies.getServiceMetricsCrud),
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
def get_all_metrics(serviceMetricsService: CRUDServiceMetric = Depends(dependencies.getServiceMetricsCrud)):
    return serviceMetricsService.list()

@router.get("/allScorecards")
def getScoreCards(
    microserviceScoreCardService: CRUDMicroserviceScoreCard = Depends(dependencies.getMicroserviceScoreCardsCrud),
    token = Depends(JWTBearer())
    ):

    teamId = decodeJWT(token)["teamId"]

    return microserviceScoreCardService.getByTeamId(teamId)
"""

# ADD NEW METRIC HERE
@router.post("/", response_model=schemas.Metric)
def createMetric(metric: schemas.MetricCreate, metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> schemas.Metric:
    metricObj = metric

    # change ' ' with '-'
    metricObj.code = format_code(metric.name)

    #if (not isinstance(metricObj.area,list)):
    #    raise JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content= jsonable_encoder({"area": "BLAH"}))
    
    """
    if (metricObj.area == None):
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content= jsonable_encoder({"Area field cannot be empty"}))
    """

    # Stringfying the list of areas to be saved as string 
    metricObj.area = json.dumps(metric.area)
    
    if (metricObj.type != "integer" and metricObj.type != "boolean"):
        raise ExceptionCustom(status_code=422, detail= "type must be integer or boolean")
    

    metricCrud.create(metricObj)
    raise ExceptionCustom(status_code=200, detail="Success in creating metric")
    #except HTTPException as exc:
    #    return ExceptionCustom(status_code=exc.status_code, detail= exc.detail)

# Get Any Metric Here By ID with parsing the list to be a real list not just stringified
@router.get("/{metricID}", response_model=schemas.List[schemas.Metric])
def getMetric(metricID: int, metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    metric = metricCrud.get(metricID)
    metric.area = json.loads(metric.area)
    metricOBJ = jsonable_encoder(metric)
    # HERE MAN IT IS NOT WORKING WITH ExceptionCustom
    raise ExceptionCustom(status_code=200, detail=metricOBJ)

@router.delete("/{metricID}")
def deleteMetric(metricID: int, metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    metric = metricCrud.get(metricID)
    if metric is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content= jsonable_encoder({"Not Found"}))
    metricCrud.delete(metricID)
    raise ExceptionCustom(status_code = 200 , detail="deleted successfully")

#Still need some work to be enhanced
@router.put("/{metricID}")
def editMetric(metricID: int, metricInput: schemas.MetricUpdate ,metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    metric = metricCrud.get(metricID)
    metricObj = metricInput
    if (metricInput.name):
        metricObj.name = metricInput.name
        metricObj.code = format_code(metricInput.name)
    if (metricInput.area):
        metricObj.area = json.dumps(metricInput.area)
    if (metricInput.description == None):
        metricObj.description = metric.description
    if (metricInput.type == None):
        metricObj.type = metric.type
    metricCrud.update(metricID,metricObj)
    raise ExceptionCustom(status_code=200, detail="Success in Editing")




@router.get("/", response_model=schemas.List[schemas.Metric])
def getAllMetrics(metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    metrics = metricCrud.list()
    metricsOBJ =  []
    for metric in metrics:
        metric.area = json.loads(metric.area)
        metricsOBJ.append(metric)
    raise ExceptionCustom(status_code=200, detail= jsonable_encoder(metricsOBJ))

    

"""
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Get the original 'detail' list of errors
    details = exc.errors()
    modified_details = []
    # Replace 'msg' with 'message' for each error
    for error in details:
        modified_details.append(
            {
                "loc": error["loc"],
            }
        )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"Message": modified_details}),
    )
"""


# JUST TRYING SMTH 
"""
Dummy_Data = [
    {"id": 1, "name": "metric1", "area": ["area1", "area2"]},
    {"id": 2, "name": "metric2", "area": ["area1", "area2"]},
    {"id": 3, "name": "metric3", "area": ["area1", "area2"]},
    {"id": 4, "name": "metric4", "area": ["area1", "area2"]},
    {"id": 5, "name": "metric5", "area": ["area1", "area2"]},
    {"id": 6, "name": "metric6", "area": ["area1", "area2"]},
    {"id": 7, "name": "metric7", "area": ["area1", "area2"]},
    {"id": 8, "name": "metric8", "area": ["area1", "area2"]},
    {"id": 9, "name": "metric9", "area": ["area1", "area2"]},
]

@router.get("/dummy", response_model=list)
def getMETRICS(Dummy_Data:list):
    for metric in Dummy_Data:
        metric["area"] = json.dumps(metric["area"])
    return Dummy_Data
"""