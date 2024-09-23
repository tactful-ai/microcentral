from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json
from app.schemas.apiResponse import CustomResponse


class ResponseCustomized(JSONResponse):
    def render(self, data) -> JSONResponse:
        if isinstance(data,str):
            content = CustomResponse(
                message = data
            )
        else:
            content = data
        content = jsonable_encoder(content, custom_encoder={bool: lambda o: o})
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")