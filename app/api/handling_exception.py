from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette import status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from app.schemas.apiException import CustomException


def my_exception_handler(request: Request, exc: HTTPException):
    if isinstance(exc.detail, str):
        content = {"message": exc.detail}
    else :
        content = exc.detail

    return JSONResponse(
        status_code=exc.status_code,
        content=content
    )

def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Get the original 'detail' list of errors
    details = exc.errors()
    modified_details = []
    for error in details:
        modified_details.append(
            {
                error["loc"][1]: error["msg"]
            }
        )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content = jsonable_encoder(CustomException(
            message="error in the datatypes",
            details=modified_details
        ))
    )