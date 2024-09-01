from . import teams, metrics, microservice, scorecard 
from fastapi import APIRouter

apiRouter = APIRouter()

apiRouter.include_router(teams.router, prefix="/teams", tags=["teams"])

apiRouter.include_router(metrics.router, prefix="/metrics", tags=["metrics"])

apiRouter.include_router(microservice.router , prefix="/services",tags=["microservice"])

apiRouter.include_router(scorecard.router, prefix="/scorecard", tags=["scorecards"])