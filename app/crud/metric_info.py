import sqlalchemy
from sqlalchemy.orm import Session
from ..schemas import MetricInfoBase
from .base import CRUDBase
from . import CRUDServiceMetric , CRUDMetric ,CRUDScoreCardMetric



class CRUDMetricInfo:
    def __init__(self, db_session: Session):
              self.servicemetric = CRUDServiceMetric(db_session)
              self.Metric = CRUDMetric(db_session)
              self.scorecardmetric = CRUDScoreCardMetric(db_session)
              
     
    def get_latest_metric_readings(self, service_id: int, scorecard_id: int) -> list[MetricInfoBase]:
      metricobjects = self.scorecardmetric.get_metrics(scorecard_id)
      metriclist= self.servicemetric.get_last_metrics(service_id,scorecard_id)       
      metric_data = {metric.metricId: metric.weight for metric in metricobjects} 
      output = []
      for metric in metriclist:
        metric_id = metric.metricId
        weight = metric_data.get(metric_id)
        
        output.append({
            'metricId': metric.metricId,          
            'metricName': self.Metric.getMetricName(metric.metricId),  
            'value': metric.value,                 
            'timestamp': metric.timestamp.strftime('%Y-%m-%d %H:%M:%S'), 
            'weight': weight if weight is not None else 0            
        })
      print("metricinfo:", output)
      return output
    
  
