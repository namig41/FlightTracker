from sqlalchemy import select

from app.bookings.models import Bookings

from app.database import async_session
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings
