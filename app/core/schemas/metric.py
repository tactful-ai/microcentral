from pydantic import BaseModel


class Metric(BaseModel):
    id: int
    name: str
    code: str
    area: str
    description: str
    type: str

    class Config:
        orm_mode = True


class MetricCreate(BaseModel):
    name: str
    code: str
    area: str
    description: str
    type: str

    class Config:
        orm_mode = True


class MetricUpdate(MetricCreate):
    pass
