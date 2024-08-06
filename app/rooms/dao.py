from app.rooms.models import Rooms

from app.database import async_session
from app.dao.base import BaseDAO


class RoomsDAO(BaseDAO):
    model = Rooms
