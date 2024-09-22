from . import teams, metrics,microservice ,microservice_info ,metric_info
from fastapi import APIRouter

apiRouter = APIRouter()

apiRouter.include_router(teams.router, prefix="/teams", tags=["teams"])

apiRouter.include_router(metrics.router, prefix="/metrics", tags=["metrics"])

apiRouter.include_router(microservice.router , prefix="/services",tags=["microservice"])

apiRouter.include_router(microservice_info.router , prefix="/serviceinfo",tags=["microserviceinfo"])

apiRouter.include_router(metric_info.router , prefix="/metricinfo",tags=["metricinfo"])