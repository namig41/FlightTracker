from app.hotels.models import Hotels

from app.database import async_session
from app.dao.base import BaseDAO


class HotelsDAO(BaseDAO):
    model = Hotels
