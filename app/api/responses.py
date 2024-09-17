from fastapi import Request
from fastapi.responses import ORJSONResponse, UJSONResponse, Response, JSONResponse
from typing import Any
from typing import Optional, Dict, Any
from fastapi.encoders import jsonable_encoder
import json
from app.schemas.apiResponse import CustomResponse


class ResponseCustomized(JSONResponse):
    def render(self, data) -> JSONResponse:
        print(data)
        
        #message = jsonable_encoder(message)
        if isinstance(data,str):
            print("message")
            content = CustomResponse(
                message = data
            )
        else:
            print("data")
            content = data
        content = jsonable_encoder(content)
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")
    """
    def response_handler(exc :JSONResponse):
        exc = jsonable_encoder(exc)
        print("Hello")
        print(exc)
        if isinstance(exc.detail, str):
            content = {"message": exc.detail}
        else:
            content = exc.detail

        return JSONResponse(
            status_code= exc.status_code,
            content = content
        )
    """