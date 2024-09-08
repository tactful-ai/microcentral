from ..schemas import serviceMetric , metric_info
from .base import CRUDBase
import sqlalchemy
from sqlalchemy.orm import Session
from . import CRUDServiceMetric 


class CRUDMetricInfo:
    def __init__(self, db_session: Session):
              self.serviceMetric = CRUDServiceMetric(db_session)
              self.metricInfo = CRUDMetricInfo(db_session)
              
  