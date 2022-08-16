from app.core.models.model import User, UserQueries
from app.database import engine
from sqlalchemy import MetaData
from sqlalchemy.orm import Session


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
        users = UserQueries(self.db)
        users.create_user(User(email="ahmedheltaher@gmdcil.com", hashed_password="super_secret_password"))
