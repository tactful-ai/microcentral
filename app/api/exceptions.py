from fastapi import HTTPException

class ExceptionCustom(HTTPException):
    pass

class MyHTTPException(HTTPException):
    pass