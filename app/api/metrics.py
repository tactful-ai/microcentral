from fastapi.exceptions import RequestValidationError
from app.schemas import ServiceMetricCreate, MetricCreate
from fastapi import APIRouter, Depends, Request, exception_handlers, status, Response, HTTPException, FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from app.crud import CRUDMetric, CRUDServiceMetric, CRUDMicroserviceScoreCard, CRUDMicroservice
from app.core.security import JWTBearer, decodeJWT
from app import schemas, models, crud, dependencies
from typing import Any, Callable
import json
from fastapi.routing import APIRoute
from .exceptions import HTTPResponseCustomized, ExceptionCustom
from app.utils.base import format_code


metric_type = ["integer", "boolean"]


class Value(BaseModel):
    value: int | bool | float | str = Field(
        ..., title="Value", description="Value of the metric")


router = APIRouter()


# ADD NEW METRIC HERE
@router.post("/", response_model=schemas.Metric)
def createMetric(metric: schemas.MetricCreate, metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> schemas.Metric:
    metricObj = metric
    # change ' ' with '-'
    metricObj.code = format_code(metric.name)
    # Stringfying the list of areas to be saved as string
    if (metricObj.area != None):
        if any(item == "" for item in metricObj.area):
            raise HTTPResponseCustomized(
                status_code=422, detail="area can not have an empty string or more")
        try:
            # I use set to remove all duplicates and return it back to list cuz set is not json serializable
            metricObj.area = list(set(metric.area))
            metricObj.area = json.dumps(metric.area)
        # Well it will throw the error but i can not test it as i dont know how the error will come as XD
        # need help for testing it.
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid area datatype: {e}")
    else:
        metric.area = []
        metricObj.area = json.dumps(metric.area)

    # Handling the datatype of the field type to be integer or boolean
    if (metricObj.type not in metric_type):
        raise HTTPResponseCustomized(
            status_code=422, detail="type must be integer or boolean")
    metricCrud.create(metricObj)
    raise HTTPResponseCustomized(
        status_code=200, detail="Success in creating metric")

# Get Any Metric Here By ID with parsing the list to be a real list not just stringified
@router.get("/{metricID}", response_model=schemas.Metric)
def getMetric(metricID: int, metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    metric = metricCrud.get(metricID)
    try:
        metric.area = json.loads(metric.area)
    except json.JSONDecodeError as e:
        metric.area = []
        metric.area = json.loads(metric.area)
    metricOBJ = jsonable_encoder(metric)
    raise HTTPResponseCustomized(status_code=200, detail=metricOBJ)

# Delete any metric using its own ID
@router.delete("/{metricID}")
def deleteMetric(metricID: int, metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    # this line is used to check if the metric is found to be deleted as
    # if it is not found this will auto raise an error "Not Found"
    metric = metricCrud.get(metricID)
    metricCrud.delete(metricID)
    raise HTTPResponseCustomized(
        status_code=200, detail="deleted successfully")


@router.put("/{metricID}")
def editMetric(metricID: int, metricInput: schemas.MetricUpdate, metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    metric = metricCrud.get(metricID)
    metricObj = metricInput
    if (metricInput.name):
        metricObj.code = format_code(metricInput.name)
        if (metricCrud.getByCode(metricObj.code) and metricObj.id == metric.id):
            raise HTTPResponseCustomized(
                status_code=422, detail="name already exists")
    if (metricInput.area != None):
        if any(item == "" for item in metricObj.area):
            raise HTTPResponseCustomized(
                status_code=422, detail="area can not have an empty string or more")
        try:
            # I use set to remove all duplicates and return it back to list cuz set is not json serializable
            metricObj.area = list(set(metricInput.area))
            metricObj.area = json.dumps(metricInput.area)
        # Well it will throw the error but i can not test it as i dont know how the error will come as XD
        # need help for testing it.
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid area datatype: {e}")
    else:
        metric.area = []
        metricObj.area = json.dumps(metric.area)
    if (metricObj.type and metricObj.type not in metric_type):
        raise HTTPResponseCustomized(
            status_code=422, detail="type must be integer or boolean")
    metricCrud.update(metricID, metricObj)
    raise HTTPResponseCustomized(status_code=200, detail="Success in Editing")

# get all the metrics


@router.get("/", response_model=schemas.List[schemas.Metric])
def getAllMetrics(metricCrud: crud.CRUDMetric = Depends(dependencies.getMetricsCrud)) -> Any:
    metrics = metricCrud.list()
    metricsOBJ = []
    for metric in metrics:
        metric.area = json.loads(metric.area)
        metricsOBJ.append(metric)
    raise HTTPResponseCustomized(
        status_code=200, detail=jsonable_encoder(metricsOBJ))
