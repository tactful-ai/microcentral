from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette import status


def my_exception_handler(request: Request, exc: HTTPException):
    if isinstance(exc.detail, str):
        content = {"message": exc.detail}
    else :
        content = exc.detail

    return JSONResponse(
        status_code=exc.status_code,
        content=content
    )