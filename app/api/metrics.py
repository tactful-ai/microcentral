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
from fastapi.routing import APIRoute




from app import dependencies 
from app.core.security import JWTBearer, decodeJWT

class Value(BaseModel):
    value: int | bool | float | str = Field(..., title="Value", description="Value of the metric")

router = APIRouter()
app = FastAPI()


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


# ADD NEW METRIC HERE
@router.post("/", response_model=schemas.Metric)
def createMetric(metric: schemas.MetricCreate, metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> schemas.Metric:
    metricObj = metric

    # change ' ' with '-'
    metricObj.code = "-".join( metric.name.split())

    if (not isinstance(metricObj.area,list)):
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content= jsonable_encoder({"area": "area must be valid list"}))
    
    """
    if (metricObj.area == None):
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content= jsonable_encoder({"Area field cannot be empty"}))
    """

    # Stringfying the list of areas to be saved as string 
    metricObj.area = json.dumps(metric.area)
    
    if (metricObj.type != "integer" and metricObj.type != "boolean"):
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content= jsonable_encoder({"type": "type must be integer or boolean"}))
    
    try:
        metricCrud.create(metricObj)
        return JSONResponse(status_code=status.HTTP_200_OK, content= jsonable_encoder({"message": "Success", "object":metricObj}))
    except HTTPException as exc:
        return JSONResponse(status_code=exc.status_code, content= jsonable_encoder({"error": exc.detail}))

# Get Any Metric Here By ID with parsing the list to be a real list not just stringified
@router.get("/{metricID}", response_model=schemas.List[schemas.Metric])
def getMetric(metricID: int, metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    metric = metricCrud.get(metricID)
    metric.area = json.loads(metric.area)
    if metric is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content= jsonable_encoder({"error":"Not Found"}))
    return JSONResponse(status_code=status.HTTP_200_OK, content= jsonable_encoder({"object":metric}))

@router.delete("/{metricID}")
def deleteMetric(metricID: int, metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    metric = metricCrud.get(metricID)
    if metric is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content= jsonable_encoder({"Not Found"}))
    metricCrud.delete(metricID)
    return JSONResponse("deleted successfully")

#Still need some work to be enhanced
@router.put("/{metricID}")
def editMetric(metricID: int, metricInput: schemas.MetricUpdate ,metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    metric = metricCrud.get(metricID)
    if metric is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content= jsonable_encoder({"Not Found"}))
    print(metric.area)
    if (metricInput.name):
        metric.name = metricInput.name
        metric.code = "-".join( metricInput.name.split())
    if (metricInput.area):
        metric.area = json.dumps(metricInput.area)
    if (metricInput.description):
        metric.description = metricInput.description
    if (metricInput.type):
        metric.type = metricInput.type
    metricCrud.update(metricID,metric)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Success in Editing")


"""
# For Older Version of Metric where area is not list 
@router.get("/", response_model=schemas.List[schemas.Metric])
def getAllMetrics(metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    return JSONResponse(status_code=status.HTTP_200_OK, content= jsonable_encoder({"object":metricCrud.list()}))
"""
    

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