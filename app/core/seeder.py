from app.database import engine
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from .models.model import User

users = [
    {
        "email": "test1@test.com",
        "hashed_password": "test1"
    },
     {
        "email": "test2@test.com",
        "hashed_password": "test2"
    }
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
        user_rows = [User(**user) for user in users]
        self.db.add_all(user_rows)
        self.db.commit()
