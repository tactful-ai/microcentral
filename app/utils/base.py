import re
from app.api.exceptions import HTTPResponseCustomized
from fastapi import Depends
from app import crud, dependencies
from app import dependencies
from fastapi.exceptions import RequestValidationError
from app.schemas import ServiceMetricCreate, MetricCreate, scoreCard, microserviceScoreCard, ScorecardServiceMetric
from fastapi import APIRouter, Depends, Request, exception_handlers, status, Response, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from app.crud import CRUDMetric, CRUDServiceMetric, CRUDMicroserviceScoreCard, CRUDMicroservice
from app import schemas, models, crud
from typing import Any, List
import json
from fastapi.routing import APIRoute
from app.models.scoreCardMetrics import criteriaStates

db_session = dependencies.get_db()
metricCrud: crud.CRUDMetric = CRUDMetric(db_session)


def format_code(name):
    code = re.sub(r'\s+', '-', name.strip())
    return code.lower()


def check_unique_ids(objects):
    id_set = set()
    for obj in objects:
        if obj.id in id_set:
            raise HTTPResponseCustomized(
                status_code=400, detail="Metrics IDs are not unique, Please don't duplicate your metric")
        id_set.add(obj.id)
    return True


def check_metric_weight(objects):
    sum = 0
    for obj in objects:
        sum += obj.weight
    if (sum == 100):
        return True
    raise HTTPResponseCustomized(
        status_code=400, detail="Sum of metric weight is not 100")


def check_metric_type(objects):
    for obj in objects:
        print(obj.type)
        print(obj.desiredValue)
        if (obj.type == "integer"):
            if (not isinstance(obj.desiredValue, int)):
                raise HTTPResponseCustomized(
                    status_code=400, detail="desierdValue is not correct for integer metric")
        elif (obj.type == "boolean"):
            if (not isinstance(obj.desiredValue, bool)):
                raise HTTPResponseCustomized(
                    status_code=400, detail="desierdValue is not correct for boolean metric")
        elif (obj.type == "string"):
            if (not isinstance(obj.desiredValue, str)):
                raise HTTPResponseCustomized(
                    status_code=400, detail="desierdValue is not correct for string metric")
        elif (obj.type == "float"):
            if (not isinstance(obj.desiredValue, float)):
                raise HTTPResponseCustomized(
                    status_code=400, detail="desierdValue is not correct for float metric")
        else:
            raise HTTPResponseCustomized(status_code=400, detail="desiredValue is not correct for anytype of metric")


#criteriaStates = ("greater", "smaller", "equal", "greater or equal", "smaller or equal")


def check_metric_criteria(objects):
    for obj in objects:
        if (obj.criteria not in criteriaStates):
            raise HTTPResponseCustomized(
                status_code=400, detail="Criteria is not correct")

        if (obj.type == "string" or obj.type == "boolean"):
            if (obj.criteria != "equal"):
                raise HTTPResponseCustomized(
                    status_code=400, detail="Criteria is not correct for this metric, you must make it equal")


def check_metric(objects):
    check_unique_ids(objects)
    check_metric_weight(objects)
    check_metric_type(objects)
    check_metric_criteria(objects)


def parse_stringified_value(value: str, target_type: str) -> int | float | bool | str:
    try:
        if target_type == 'boolean':
            if value.lower() in ('true', '1'):
                return True
            elif value.lower() in ('false', '0'):
                return False
            else:
                raise ValueError(f"Cannot convert {value} to boolean.")
        elif target_type == 'integer':
            try:
                return int(value)
            except ValueError:
                raise ValueError(f"Cannot convert {value} to integer.")
        elif target_type == 'float':
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"Cannot convert {value} to float.")
        elif target_type == 'string':
            return value
    except:
        raise ValueError(f"Unsupported target type: {target_type}")


def stringify_value(value) -> str:
    if isinstance(value, bool):
        return 'True' if value else 'False'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return value
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")
