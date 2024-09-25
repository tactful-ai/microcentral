import sqlalchemy
from sqlalchemy.orm import Session
from ..schemas import MetricInfoBase
from .base import CRUDBase
from . import CRUDServiceMetric, CRUDMetric, CRUDScoreCardMetric


class CRUDMetricInfo:
    def __init__(self, db_session: Session):
        self.servicemetric = CRUDServiceMetric(db_session)
        self.Metric = CRUDMetric(db_session)
        self.scorecardmetric = CRUDScoreCardMetric(db_session)

    def get_latest_metric_readings(self, service_id: int, scorecard_id: int) -> list[MetricInfoBase]:
        scoremetricobjects = self.scorecardmetric.get_metrics(scorecard_id)
        metriclist = self.servicemetric.get_last_metrics( scorecard_id ,service_id)
        metric_data = {
            metric.metricId: metric.weight for metric in scoremetricobjects}
        metric_ids = [metric.metricId for metric in metriclist]

        metrics = self.Metric.get_all_by_ids(metric_ids)
        metric_names = {metric.id: metric.name for metric in metrics}

        output = [{
            'metricId': metric.metricId,
            'metricName': metric_names[metric.metricId],
            'value': metric.value,
            'timestamp': metric.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'weight': metric_data[metric.metricId]
        } for metric in metriclist]
        return output
