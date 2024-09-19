from sqlalchemy.orm import Session
from app.schemas.scorecardServiceMetric import ScorecardServiceMetricCreate, ScorecardServiceMetric, ScorecardServiceMetricUpdate
from . import CRUDScoreCardMetric, CRUDMicroserviceScoreCard, CRUDMetric, CRUDScoreCard, CRUDMicroservice
from .base import CRUDBase
from app.utils import format_code
from app.utils.base import parse_stringified_value
from app.schemas.microservice import Microserviceforscorecard
from app.schemas.scoreCardMetrics import MetricListforScorecardGet

class CRUDScoreCardServiceMetric(CRUDBase[ScorecardServiceMetric, ScorecardServiceMetricCreate, ScorecardServiceMetricUpdate]):
    def __init__(self, db_session: Session):
        self.scoreCard = CRUDScoreCard(db_session)
        self.microServiceScoreCard = CRUDMicroserviceScoreCard(db_session)
        self.scoreCardMetric = CRUDScoreCardMetric(db_session)
        self.microService = CRUDMicroservice(db_session)
        self.metric = CRUDMetric(db_session)

    def getwithscorecardIDmetricandservice(self, scorecardID: int):
        # it handles if the scorecard is not found & raises error message
        scorecard = self.scoreCard.get(scorecardID)

        # get ids of metrics and services used in this scorecard
        metrics = self.scoreCardMetric.getbyscorecardID(scorecardID)
        services = self.microServiceScoreCard.getservice(scorecardID)
        metric_ids = [sc_id.metricId for sc_id in metrics]
        service_ids = [sc_id.microserviceId for sc_id in services]

        metricOBJs = []
        serviceOBJs = []

        metrics = self.metric.getByIds(metric_ids)
        metrics_types_map = {metric.id : metric.type for metric in metrics}
        metricList = self.scoreCardMetric.getByMetricIdsandScorecardId(
            metric_ids, scorecardID)
        for metric in metricList:
            metrictype = metrics_types_map[metric.metricId]
            print(metrictype)
            metric.desiredValue = parse_stringified_value(metric.desiredValue, metrictype)
            metricOBJs.append({
                'id': metric.metricId,
                'criteria': metric.criteria,
                'desiredValue': metric.desiredValue,
                'weight': metric.weight
            })

        serviceList = self.microService.getByServiceIds(service_ids)
        serviceOBJs = [Microserviceforscorecard(**vars(service)) for service in serviceList]

        scorecard.code = format_code(scorecard.name)
        scorecard = ScorecardServiceMetric(
            id=scorecard.id,
            name=scorecard.name,
            code=scorecard.code,
            description=scorecard.description,
            metrics=metricOBJs,
            services=serviceOBJs
        )
        return scorecard.dict()

    def getlist(self):
        # Got all the scorecard ids i want
        scorecards = self.scoreCard.list()
        scorecardIDs = []
        for scorecard in scorecards:
            scorecardIDs.append(scorecard.id)
        out = []
        for scorecardID in scorecardIDs:
            # it handles if the scorecard is not found & raises error message
            scorecard = self.scoreCard.get(scorecardID)

            # get ids of metrics and services used in this scorecard
            metrics = self.scoreCardMetric.getbyscorecardID(scorecardID)
            services = self.microServiceScoreCard.getservice(scorecardID)
            metric_ids = [sc_id.metricId for sc_id in metrics]
            service_ids = [sc_id.microserviceId for sc_id in services]
            
            metricOBJs = []
            serviceOBJs = []

            metrics = self.metric.getByIds(metric_ids)
            metrics_types_map = {metric.id : metric.type for metric in metrics}
            metricList = self.scoreCardMetric.getByMetricIdsandScorecardId(metric_ids, scorecardID)
            for metric in metricList:
                metrictype = metrics_types_map[metric.metricId]
                metric.desiredValue = parse_stringified_value(metric.desiredValue, metrictype)
                metricOBJs.append(MetricListforScorecardGet(**vars(metric)))

            serviceList = self.microService.getByServiceIds(service_ids)
            serviceOBJs = [Microserviceforscorecard(**vars(service)) for service in serviceList]

            scorecard.code = format_code(scorecard.name)
            scorecardOut = ScorecardServiceMetric(
                id=scorecard.id,
                name=scorecard.name,
                code=scorecard.code,
                description=scorecard.description,
                metrics=metricOBJs,
                services=serviceOBJs
            )
            out.append(scorecardOut.dict())
        return out
