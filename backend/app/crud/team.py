from sqlalchemy.orm import Session

from ..models import Team
from ..schemas.team import TeamCreate, TeamUpdate
from .base import CRUDBase


class CRUDTeam(CRUDBase[Team, TeamCreate, TeamUpdate]):
    def __init__(self, db_session: Session):
        super(CRUDTeam, self).__init__(Team, db_session)
