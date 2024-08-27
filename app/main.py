from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import Request, status, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from app.api.exceptions import ExceptionCustom
from app.api.handling_exception import my_exception_handler

from app.api.api import apiRouter
from app.core.config import settings
from app.views.dashboard import router as dashboard_router


def create_app() -> FastAPI:
    _app = FastAPI(title=settings.PROJECT_NAME, description=settings.PROJECT_DESCRIPTION, version=settings.PROJECT_VERSION)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.add_exception_handler(ExceptionCustom, my_exception_handler)

    
    # Edit on the exceptiion handler of data type validation pydantic to send custom error messages
    @_app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        # Get the original 'detail' list of errors
        details = exc.errors()
        modified_details = []
        # Replace 'msg' with 'message' for each error
        for error in details:
            modified_details.append(
                {
                    error["loc"][1]: error["msg"]
                }
            )
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"message": modified_details}),
        )
    
    
    """
    class ExceptionCustom(HTTPException):
        pass
    def exception_404_handler(request: Request, exc: HTTPException):
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message":exc.detail})
    _app.add_exception_handler(ExceptionCustom, exception_404_handler)
    """
    
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