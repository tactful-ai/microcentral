from fastapi import APIRouter, Depends
from typing import List
from app import dependencies
from pydantic import BaseModel, Field
from .exceptions import ExceptionCustom
from app.schemas import MetricInfoBase
from app.crud import CRUDMetricInfo


class Value(BaseModel):
    value: int | bool | float | str = Field(
        ..., title="Value", description="Value of the metricinfo")


router = APIRouter()


@router.get("/{service_id}/{scorecard_id}", response_model=List[MetricInfoBase])
def get_latest_metrics(service_id: int, scorecard_id: int, metricInfo:CRUDMetricInfo = Depends(dependencies.getMetricInfoCrud)):
    metrics = metricInfo.get_latest_metric_readings(service_id, scorecard_id)
    print(metrics)
    if not metrics:
        raise ExceptionCustom(status_code=404, detail="metrics not found")
    return metrics


