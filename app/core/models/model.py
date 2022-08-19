import uuid

from app.database import Base
from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return "<User(email='%s')>" % self.email

