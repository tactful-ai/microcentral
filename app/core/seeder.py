from app.database import engine
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from .models import Metric, Microservice, Scorecard, ServiceMetric, Team

teams = [
    {
        'name': 'Team 1'
    },
    {
        'name': 'Team 2'
    },
    {
        'name': 'Team 3'
    },
]

microservices = [
    {
        'name': 'Microservice 1',
        'description': 'This is microservice 1',
        'team_id': 1,
    },
    {
        'name': 'Microservice 2',
        'description': 'This is microservice 2',
        'team_id': 1,
    },
    {
        'name': 'Microservice 3',
        'description': 'This is microservice 3',
        'team_id': 2,
    },
    {
        'name': 'Microservice 4',
        'description': 'This is microservice 4',
        'team_id': 2,
    },
    {
        'name': 'Microservice 5',
        'description': 'This is microservice 5',
        'team_id': 3,
    },
    {
        'name': 'Microservice 6',
        'description': 'This is microservice 6',
        'team_id': 3,
    },
]

metrics = [
    {
        'area': 'Metric 1',
        'description': 'This is metric 1',
        'type': 1,
    },
    {
        'area': 'Metric 2',
        'description': 'This is metric 2',
        'type': 1,
    },
    {
        'area': 'Metric 3',
        'description': 'This is metric 3',
        'type': 1,
    },
    {
        'area': 'Metric 4',
        'description': 'This is metric 4',
        'type': 1,
    },
    {
        'area': 'Metric 5',
        'description': 'This is metric 5',
        'type': 1,
    },
    {
        'area': 'Metric 6',
        'description': 'This is metric 6',
        'type': 1,
    }
]

scorecards = [
    {
        'name': 'Scorecard 1',
        'description': 'This is scorecard 1',
        'microservice_id': 1
    } ,
    {
        'name': 'Scorecard 2',
        'description': 'This is scorecard 2',
        'microservice_id': 1
    } ,
    {
        'name': 'Scorecard 3',
        'description': 'This is scorecard 3',
        'microservice_id': 2
    } ,
    {
        'name': 'Scorecard 4',
        'description': 'This is scorecard 4',
        'microservice_id': 2
    } ,
    {
        'name': 'Scorecard 5',
        'description': 'This is scorecard 5',
        'microservice_id': 3
    } ,
    {
        'name': 'Scorecard 6',
        'description': 'This is scorecard 6',
        'microservice_id': 3
    } ,
]

service_metrics = [
    {
        'metric_id': 1,
        'scorecard_id': 1,
        'value': 1
    } ,
    {
        'metric_id': 2,
        'scorecard_id': 1,
        'value': 2
    } ,
    {
        'metric_id': 3,
        'scorecard_id': 1,
        'value': 3
    } ,
    {
        'metric_id': 4,
        'scorecard_id': 1,
        'value': 4
    } ,
    {
        'metric_id': 5,
        'scorecard_id': 1,
        'value': 5
    } ,
    {
        'metric_id': 6,
        'scorecard_id': 1,
        'value': 6
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
