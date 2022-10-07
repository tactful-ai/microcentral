from functools import lru_cache
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: Optional[str] = ""
    PROJECT_VERSION: Optional[str] = "1.0.0"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


    API_V1_STR: str = "/api/v1"

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_DATABASE: str
    DATABASE_URI: Optional[PostgresDsn] = None

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30 # 30 days

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, value: Optional[PostgresDsn], values: Dict[str, Any]) -> Any:
        if isinstance(value, PostgresDsn):
            return value
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DB_USER"),
            password=values.get("DB_PASSWORD"),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),
            path=f"/{values.get('DB_DATABASE') or ''}",
        )

    class Config:
        case_sensitive = True
        env_file = "../env"


# This is a decorator that caches the result of the function
# so that it doesn't have to be called again
@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
