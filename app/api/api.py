from . import teams, metrics, scorecard
from fastapi import APIRouter

apiRouter = APIRouter()

apiRouter.include_router(teams.router, prefix="/teams", tags=["teams"])

apiRouter.include_router(metrics.router, prefix="/metrics", tags=["metrics"])

apiRouter.include_router(scorecard.router, prefix="/scorecard", tags=["scorecards"])