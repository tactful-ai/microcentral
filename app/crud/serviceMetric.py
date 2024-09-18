from sqlalchemy.orm import Session

from sqlalchemy import func, and_, select
from ..models import ServiceMetric, scoreCardMetrics, Metric
from ..schemas import ServiceMetricCreate, ServiceMetricUpdate, ServiceMetricReading
from .base import CRUDBase
from . import CRUDScoreCardMetric, CRUDMetric
from app.utils.utility_functions import main_calculate_error, calculate_score
from typing import Optional
from datetime import datetime


class CRUDServiceMetric(CRUDBase[ServiceMetric, ServiceMetricCreate, ServiceMetricUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDServiceMetric, self).__init__(ServiceMetric, db_session)
        self.scorecardMetrics = CRUDScoreCardMetric(db_session)
        self.Metric = CRUDMetric(db_session)

    def getByScorecardId(self, scorecardId: int) -> list[ServiceMetric]:
        return self.db_session.query(ServiceMetric).filter(ServiceMetric.scorecardId == scorecardId).all()

    def getByServiceId(self, serviceId: int) -> list[ServiceMetric]:
        return self.db_session.query(ServiceMetric).filter(ServiceMetric.serviceId == serviceId).all()

    def get_metric_values_by_service(self, service_id: int, from_date: Optional[datetime], to_date: Optional[datetime]) -> list[ServiceMetricReading]:

        query = self.db_session.query(ServiceMetric.metricId, ServiceMetric.value, ServiceMetric.timestamp).filter(
            ServiceMetric.serviceId == service_id)
        if from_date and to_date:
            query = query.filter(ServiceMetric.timestamp >=
                                 from_date, ServiceMetric.timestamp <= to_date)
        elif from_date:
            query = query.filter(ServiceMetric.timestamp >= from_date)
        elif to_date:
            query = query.filter(ServiceMetric.timestamp <= to_date)

        query = query.order_by(ServiceMetric.timestamp.desc())
        metrics = query.all()
        return metrics

    def get_last_metrics(self, scorecard_id: int, service_id: int) -> list[ServiceMetric]:
        subquery = self.db_session.query(
            ServiceMetric.metricId,
            ServiceMetric.value,
            ServiceMetric.timestamp
        ).filter(
            ServiceMetric.serviceId == service_id,
            ServiceMetric.metricId.in_(
                self.scorecardMetrics.getMetricByScoreCradId(scorecard_id))
        ).order_by(ServiceMetric.metricId, ServiceMetric.timestamp.desc()).distinct(ServiceMetric.metricId).all()
        return subquery

    def get_timestamp(self, service_id: int, scorecard_id: int):
        subquery = self.scorecardMetrics.getMetricByScoreCradId(scorecard_id)

        update_time = self.db_session.query(ServiceMetric.timestamp)\
            .filter(ServiceMetric.serviceId == service_id, ServiceMetric.metricId.in_(subquery))\
            .order_by(ServiceMetric.timestamp.desc())\
            .first()

        if update_time:
            formatted_time = update_time.timestamp.strftime(
                '%Y-%m-%d %H:%M:%S')
            return formatted_time
        else:
            return None

    def get_calculated_value(self, service_id: int, scorecard_id: int):
        scorecard_metrics = self.scorecardMetrics.get_metrics(scorecard_id)
        metric_ids = {metric.metricId for metric in scorecard_metrics}
        metrics = self.Metric.get_all_by_ids(metric_ids)
        metric_types = {metric.id: metric.type for metric in metrics}
        metric_info_dict = {

            metric.metricId: (
                metric.criteria,
                metric.desiredValue,
                metric.weight,
                metric_types[metric.metricId]
            )
            for metric in scorecard_metrics
        }
        service_metrics = self.get_last_metrics(scorecard_id, service_id)
        scorevalue = 0
        updatetime = datetime.min
        for service_metric in service_metrics:
            criteria, desired_value, weight, metric_type = metric_info_dict.get(
                service_metric.metricId)

            if criteria is not None and desired_value is not None:

                error = main_calculate_error(
                    service_metric.value, desired_value, weight, criteria, metric_type)
                score = calculate_score(error, weight)
                scorevalue += score
                updatetime = max(service_metric.timestamp, updatetime)
        return (scorevalue, updatetime)
