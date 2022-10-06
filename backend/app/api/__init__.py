from fastapi import FastAPI

from .metric import router as metric_router


def setup_routes(app: FastAPI):
    app.include_router(metric_router)
