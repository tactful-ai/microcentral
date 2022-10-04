import time
from typing import Dict

import jwt
from app.core.config import get_settings
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


def signJWT(teamId: str) -> str:
    payload = {
        "teamId": teamId,
    }
    token = jwt.encode(payload, get_settings().JWT_SECRET_KEY, algorithm=get_settings().JWT_ALGORITHM)

    return token


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, get_settings().JWT_SECRET_KEY, algorithms=[get_settings().JWT_ALGORITHM], options={"verify_exp": False})
        return decoded_token
    except:
        return {}

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtToken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtToken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
