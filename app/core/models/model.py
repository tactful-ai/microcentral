from app.database import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Session


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return "<User(email='%s')>" % self.email


class UserQueries:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_id(self, id: int) -> User:
        return self.db.query(User).filter(User.id == id).first()

    def get_all_users(self) -> list:
        return self.db.query(User).all()
    
    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        return user

    def update_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        return user
    
    def delete_user(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
