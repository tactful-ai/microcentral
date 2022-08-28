from app.core.models import Team
from app.core.schemas.team import TeamCreate, TeamUpdate
from sqlalchemy.orm import Session

from .base import BaseService


class TeamsService(BaseService[Team, TeamCreate, TeamUpdate]):
    def __init__(self, db_session: Session):
        super(TeamsService, self).__init__(Team, db_session)
