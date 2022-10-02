from sqlalchemy.orm import Session

from ...core.models import Team
from ...core.schemas.team import TeamCreate, TeamUpdate
from .base import BaseService


class TeamsService(BaseService[Team, TeamCreate, TeamUpdate]):
    def __init__(self, db_session: Session):
        super(TeamsService, self).__init__(Team, db_session)
