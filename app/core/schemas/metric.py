from pydantic import BaseModel


class Metric(BaseModel):
    id: int
    area: str
    description: str
    type: int

    class Config:
        orm_mode = True


class MetricCreate(BaseModel):
    area: str
    description: str
    type: int

    class Config:
        orm_mode = True


class MetricUpdate(BaseModel):
    area: str
    description: str
    type: int = None

    class Config:
        orm_mode = True
