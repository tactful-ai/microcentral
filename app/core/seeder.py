from app.database import engine
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from .models import Metric, Microservice, Scorecard, ServiceMetric, Team

teams = [
    {
        'name': 'Marketing'
    },
    {
        'name': 'Pr'
    },
    {
        'name': 'Operation'
    },
    {
        'name': 'Technical'
    },
    {
        'name': 'Hr'
    },
]

microservices = [
    {
        'name': 'Delivery',
        'description': 'Concerned by the timing of delivering the product.',
        'team_id': 4,
    },
    {
        'name': 'Payment Service',
        'description': 'Online payments & Salary.',
        'team_id': 5,
    },
    {
        'name': 'Financial Service',
        'description': 'Service related to assets such as banks, investments funds and tax preparation.',
        'team_id': 3,
    },
    {
        'name': 'Design',
        'description': 'Services to create designs such as graphic designs.',
        'team_id': 1,
    },
    {
        'name': 'Event Service',
        'description': 'Planning and delivery of events.',
        'team_id': 2,
    },

]

metrics = [
    {
        'area': 'Performance',
        'description': 'Performance description',
        'type': 1,
    },
    {
        'area': 'SLA and Availability',
        'description': 'Service is online and responding 99.9% of the time',
        'type': 2,
    },
    {
        'area': 'Reliability',
        'description': 'Number of error or failed sessions are below 99.9%',
        'type': 2,
    },
    {
        'area': 'Statefulness',
        'description': 'Impacts scale',
        'type': 1,
    },
    {
        'area': 'CI/CD',
        'description': 'has automated CI pipeline',
        'type': 1,
    },
]

scorecards = [
    {
        'name': 'Service Agility and Quality',
        'description': 'Measure how work is done',
        'microservice_id': 1
    } ,
    {
        'name': 'Operational Readiness',
        'description': 'Operational Readiness description',
        'microservice_id': 2
    } ,
    {
        'name': 'Service Autonomy',
        'description': 'Service Autonomy description',
        'microservice_id': 3
    } ,
    {
        'name': 'Team performance',
        'description': 'Team performance description',
        'microservice_id': 4
    } ,
    {
        'name': 'Performance and Scaling readiness',
        'description': 'Performance and Scaling readiness description ',
        'microservice_id': 5
    } ,
]

service_metrics = [
    {
        'metric_id': 2,
        'scorecard_id': 2,
        'value': 2,
        'timestamp': '2020-01-01 00:00:00'
    } ,
    {
        'metric_id': 2,
        'scorecard_id': 2,
        'value': 1,
        'timestamp': '2020-01-02 00:00:00'
    } ,
        {
        'metric_id': 2,
        'scorecard_id': 2,
        'value': 6,
        'timestamp': '2020-01-04 00:00:00'
    } ,
        {
        'metric_id': 2,
        'scorecard_id': 2,
        'value': 5,
        'timestamp': '2020-01-05 00:00:00'
    } ,
        {
        'metric_id': 2,
        'scorecard_id': 2,
        'value': 6,
        'timestamp': '2020-01-06 00:00:00'
    } ,
        {
        'metric_id': 2,
        'scorecard_id': 2,
        'value': 6,
        'timestamp': '2020-01-09 00:00:00'

    } ,
        {
        'metric_id': 2,
        'scorecard_id': 2,
        'value': 7,
        'timestamp': '2020-01-11 00:00:00'
    } ,
        {
        'metric_id': 2,
        'scorecard_id': 2,
        'value': 4,
        'timestamp': '2020-01-12 00:00:00'
    } ,
        {
        'metric_id': 2,
        'scorecard_id': 2,
        'value': 5,
        'timestamp': '2020-01-13 00:00:00'
    } ,
        {
        'metric_id': 2,
        'scorecard_id': 2,
        'value': 8,
        'timestamp': '2020-01-17 00:00:00'
    } ,
]


class Seeder:
    def __init__(self, db: Session):
        self.db = db
        self.meta = MetaData(bind=engine)
        self.meta.reflect(bind=engine)

    def create_tables(self):
        self.meta.create_all(bind=engine)

    def drop_tables(self):
        self.meta.drop_all(bind=engine)

    def seed(self):
        print("Dropping tables...")
        self.drop_tables()
        print("Tables dropped.")
        print("Creating tables...")
        self.create_tables()
        print("Tables created.")
        print("Seeding...")
        self.run()
        print("Seeding complete.")

    def run(self):

        team_rows = [Team(**team) for team in teams]
        self.db.add_all(team_rows)

        microservice_rows = [Microservice(**microservice) for microservice in microservices]
        self.db.add_all(microservice_rows)

        metric_rows = [Metric(**metric) for metric in metrics]
        self.db.add_all(metric_rows)

        scorecard_rows = [Scorecard(**scorecard) for scorecard in scorecards]
        self.db.add_all(scorecard_rows)

        service_metric_rows = [ServiceMetric(**service_metric) for service_metric in service_metrics]
        self.db.add_all(service_metric_rows)

        self.db.commit()
