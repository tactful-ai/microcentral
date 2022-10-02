from sqlalchemy.orm import Session


class Seeder:
    def __init__(self, db: Session):
        self.db = db

    def seed(self):
        pass

    def run(self):
        pass
