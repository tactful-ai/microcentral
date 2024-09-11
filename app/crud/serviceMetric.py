
from sqlalchemy.orm import Session
from ..models import ServiceMetric, scoreCardMetrics
from ..schemas import ServiceMetricCreate, ServiceMetricUpdate
from .base import CRUDBase
from . import CRUDScoreCardMetric ,CRUDMetric
from app.utils.utility_functions import main_calculate_error, calculate_score


class CRUDServiceMetric(CRUDBase[ServiceMetric, ServiceMetricCreate, ServiceMetricUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDServiceMetric, self).__init__(ServiceMetric, db_session)
        self.scorecardMetrics = CRUDScoreCardMetric(db_session)
        self.Metric = CRUDMetric(db_session)

    def getByScorecardId(self, scorecardId: int) -> list[ServiceMetric]:
        return self.db_session.query(ServiceMetric).filter(ServiceMetric.scorecardId == scorecardId).all()

    def getByServiceId(self, serviceId: int) -> list[ServiceMetric]:
        return self.db_session.query(ServiceMetric).filter(ServiceMetric.serviceId == serviceId).all()
    

    def get_timestamp(self, service_id: int, scorecard_id: int):
        subquery = self.scorecardMetrics.getMetricByScoreCradId(scorecard_id)

        update_time = self.db_session.query(ServiceMetric.timestamp)\
            .filter(ServiceMetric.serviceId == service_id, ServiceMetric.metricId.in_(subquery))\
            .order_by(ServiceMetric.timestamp.desc())\
            .first()

        if update_time:
          formatted_time = update_time.timestamp.strftime('%Y-%m-%d %H:%M:%S')
          return formatted_time
        else:
         return None

 
    def get_calculated_value(self, service_id: int, scorecard_id: int):
     scorecard_metrics = self.scorecardMetrics.get_metric(scorecard_id)
     print("Scorecard metrics:", scorecard_metrics)
     metric_info_dict = {
        metric.metricId: (metric.criteria, metric.desiredValue, metric.weight)
        for metric in scorecard_metrics
      }

     metric_info_dict = {}
     for metric in scorecard_metrics:
        metric_type = self.Metric.getMetricType(metric.metricId) 
        metric_info_dict[metric.metricId] = (
            metric.criteria,
            metric.desiredValue,
            metric.weight,
            metric_type
        )
     
     service_metrics = self.db_session.query(
        ServiceMetric.metricId,
        ServiceMetric.value,
        ServiceMetric.timestamp
     ).filter(
        ServiceMetric.serviceId == service_id,
        ServiceMetric.metricId.in_(metric_info_dict)
    # ).all()   
     ).order_by(ServiceMetric.metricId, ServiceMetric.timestamp.desc()).distinct(ServiceMetric.metricId).all()

     print("Service metrics:", service_metrics)
     scorevalue = 0
     for service_metric in service_metrics:
        criteria, desired_value , weight, metric_type  = metric_info_dict.get(service_metric.metricId)
        
        if criteria is not None and desired_value is not None:

            error = main_calculate_error(service_metric.value, desired_value,weight, criteria, metric_type)
            score = calculate_score(error, weight)
            scorevalue+= score
            print( score )
            print(scorevalue)
            print(service_metric.metricId)
     return scorevalue
  
     
 

