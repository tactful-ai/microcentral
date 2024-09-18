from sqlalchemy.orm import Session
from ..models import Team
from ..schemas import TeamCreate, TeamUpdate
from .base import CRUDBase


class CRUDTeam(CRUDBase[Team, TeamCreate, TeamUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDTeam, self).__init__(Team, db_session)

    def create(self, obj: TeamCreate) -> Team:
        db_obj: Team = super(CRUDTeam, self).create(obj)
        db_obj.token = str(db_obj.id) + "token" # TODO: generate token
        self.db_session.commit()
        return db_obj
