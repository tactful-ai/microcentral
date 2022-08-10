from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.v1.test import router as test_api_router
from app.core.config import settings
from app.views.test import router as test_view_router


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

app.include_router(test_api_router, prefix="/api/v1")
app.include_router(test_view_router, prefix="/views")

