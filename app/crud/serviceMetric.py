
from sqlalchemy.orm import Session
from ..models import ServiceMetric, scoreCardMetrics
from ..schemas import ServiceMetricCreate, ServiceMetricUpdate
from .base import CRUDBase
from . import CRUDScoreCardMetric
from app.utils.utility_functions import calculate_error, calculate_score


class CRUDServiceMetric(CRUDBase[ServiceMetric, ServiceMetricCreate, ServiceMetricUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDServiceMetric, self).__init__(ServiceMetric, db_session)
        self.scorecardMetrics = CRUDScoreCardMetric(db_session)

    def getByScorecardId(self, scorecardId: int) -> list[ServiceMetric]:
        return self.db_session.query(ServiceMetric).filter(ServiceMetric.scorecardId == scorecardId).all()

    def getByServiceId(self, serviceId: int) -> list[ServiceMetric]:
        return self.db_session.query(ServiceMetric).filter(ServiceMetric.serviceId == serviceId).all()
    
    #def get_service_metrics(db_session: Session, service_id: int, metric_info_dict: Dict[int, any]) -> List[Tuple[int, float]]:
    # service_metrics = db_session.query(
    #    ServiceMetric.metricId,
    #    ServiceMetric.value
    # ).filter(
    #    ServiceMetric.serviceId == service_id,
    #    ServiceMetric.metricId.in_(metric_info_dict)
    # ).all()

    # return service_metrics

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
     metric_info_dict = {metric.metricId: (metric.criteria, metric.desiredValue) for metric in scorecard_metrics}
    
     service_metrics = self.db_session.query(
        ServiceMetric.metricId,
        ServiceMetric.value
     ).filter(
        ServiceMetric.serviceId == service_id,
        ServiceMetric.metricId.in_(metric_info_dict)
     ).all()   
     print("Service metrics:", service_metrics)

     for service_metric in service_metrics:
        criteria, desired_value = metric_info_dict.get(service_metric.metricId)

        if criteria is not None and desired_value is not None:
            error = calculate_error(service_metric.value, desired_value, criteria)
            score = calculate_score(error)

            return score

     return None 
  
  


