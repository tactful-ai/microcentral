from pydantic import BaseModel


class Metric(BaseModel):
    id: int
    area: str
    description: str
    type: str

    class Config:
        orm_mode = True


class MetricCreate(BaseModel):
    area: str
    description: str
    type: str

    class Config:
        orm_mode = True


class MetricUpdate(BaseModel):
    area: str
    description: str
    type: str = None

    class Config:
        orm_mode = True
