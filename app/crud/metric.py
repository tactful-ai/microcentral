from sqlalchemy.orm import Session
from ..models import Metric
from ..schemas import MetricCreate, MetricUpdate
from .base import CRUDBase


class CRUDMetric(CRUDBase[Metric, MetricCreate, MetricUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDMetric, self).__init__(Metric, db_session)

    def getByCode(self, code: str):
        return self.db_session.query(Metric).filter(Metric.code == code).first()
    
    def getIdByCode(self, code: str):
        return self.db_session.query(Metric).filter(Metric.code == code).first().id()
    
    def getById(self, id:int):
        #return self.db_session.query(Metric).filter(Metric.id.in_(id)).all()
        return self.db_session.query(Metric).filter(Metric.id == id).first()
    
    def getByIds(self , ids:list[int]):
        return self.db_session.query(Metric).filter(Metric.id.in_(ids)).all()
    
    def getByName(self, name: str):
        return self.db_session.query(Metric).filter(Metric.name == name).first()
    
    def getnamebyid(self, metricID: int):
        return self.db_session.query(Metric).filter(Metric.id == metricID).first().name

