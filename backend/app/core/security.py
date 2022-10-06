from datetime import datetime, timedelta
from typing import Any, Union

import jwt
from app.core.config import get_settings


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=get_settings().ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, get_settings().JWT_SECRET_KEY, algorithm=get_settings().JWT_ALGORITHM)
    return encoded_jwt
