from typing import Any, Generic, List, Optional, Type, TypeVar

import sqlalchemy
from app.database.base_class import Base
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], db_session: Session):
        self.model = model
        self.db_session = db_session

    def get(self, id: Any) -> Optional[ModelType]:
        obj: Optional[ModelType] = self.db_session.query(self.model).get(id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj

    def list(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return self.db_session.query(self.model).offset(skip).limit(limit).all()

    def create(self, obj: CreateSchemaType) -> ModelType:
        db_obj: ModelType = self.model(**obj.dict())
        self.db_session.add(db_obj)
        try:
            self.db_session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            self.db_session.rollback()
            if "duplicate key" in str(e):
                raise HTTPException(status_code=409, detail="Duplicated Key, Name field is Duplicated")
            else:
                raise e
        return db_obj

    def update(self, id: Any, obj: UpdateSchemaType) -> Optional[ModelType]:
        db_obj = self.get(id)
        for column, value in obj.dict(exclude_unset=True).items():
            setattr(db_obj, column, value)
        self.db_session.commit()
        return db_obj

    def delete(self, id: Any) -> None:
        db_obj = self.db_session.query(self.model).get(id)
        self.db_session.delete(db_obj)
        self.db_session.commit()
