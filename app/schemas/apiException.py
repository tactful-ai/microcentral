from pydantic import BaseModel

class CustomException(BaseModel):
  message : str
  details : list[object]