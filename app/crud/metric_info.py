import sqlalchemy
from sqlalchemy.orm import Session
from ..schemas import serviceMetric , metric_info , scoreCardMetrics,MetricInfoBase
from .base import CRUDBase
from . import CRUDServiceMetric , CRUDMetric ,CRUDScoreCardMetric



class CRUDMetricInfo:
    def __init__(self, db_session: Session):
              self.servicemetric = CRUDServiceMetric(db_session)
              self.Metric = CRUDMetric(db_session)
              self.scorecardmetric = CRUDScoreCardMetric(db_session)
              
     
    def get_latest_metric_readings(self, service_id: int, scorecard_id: int) -> list[MetricInfoBase]:
      metricweights= self.scorecardmetric.getMetricWeight(scorecard_id)
      metriclist= self.servicemetric.get_last_metrics(service_id,scorecard_id)       
     
      output = []
    
      for metric in metriclist:
        output.append({
            'metricId': metric.metricId,          
            'metricName': self.Metric.getMetricName(metric.metricId),  
            'value': metric.value,                 
            'timestamp': metric.timestamp.strftime('%Y-%m-%d %H:%M:%S'), 
            'weight': metricweights             
        })
      print("metricinfo:", output)
      return output
    #def get_latest_metric_readings(self, service_id: int, scorecard_id: int):
    ## Get the list of latest metrics
    # metriclist = self.servicemetric.get_last_metrics(service_id, scorecard_id)

    # metric_ids = [metric.metricId for metric in metriclist]

    # metric_names = self.Metric.getMetricNamesByIds(metric_ids)  

    # metric_name_map = {metric_id: metric_names[metric_id] for metric_id in metric_ids}

    # output = []

    # for metric in metriclist:
    #    output.append({
    #        'metricId': metric.metricId,
    #        'metricName': metric_name_map.get(metric.metricId, 'Unknown'),  
    #        'value': metric.value,
    #        'timestamp': metric.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
    #        'weight': metric.weight
    #    })

    # return output
