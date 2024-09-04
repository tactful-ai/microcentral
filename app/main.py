from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import Request, status, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from app.api.exceptions import HTTPResponseCustomized
from app.api.handling_exception import my_exception_handler, validation_exception_handler

from app.api.api import apiRouter
from app.core.config import settings
from app.views.dashboard import router as dashboard_router


def create_app() -> FastAPI:
    _app = FastAPI(title=settings.PROJECT_NAME, description=settings.PROJECT_DESCRIPTION, version=settings.PROJECT_VERSION)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.add_exception_handler(HTTPResponseCustomized, my_exception_handler)

    @_app.exception_handler(RequestValidationError)
    async def ValidationExceptionHandler(request: Request, exc: RequestValidationError):
        return validation_exception_handler(request, exc)

    # Just for checking if the app is up and running
    @_app.get("/health")
    async def health() -> str:
        return "ok"

    _app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

    # setup_routes(_app)
    _app.include_router(dashboard_router, prefix="/dashboard")
    _app.include_router(apiRouter, prefix=settings.API_V1_STR)

    return _app


app = create_app()
