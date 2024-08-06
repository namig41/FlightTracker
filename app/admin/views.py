from app.users.models import Users
from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.rooms.models import Rooms

from sqladmin import ModelView


class UserAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class BookingsAdmin(ModelView, model=Bookings):
    column_list = [c.name for c in Bookings.__table__.c] + [Users.booking]
    column_details_exclude_list = [Users.hashed_password]
    name = "Бронь"
    name_plural = "Брони"
    icon = "fa-solid fa-user"


class RoomsAdmin(ModelView, model=Rooms):
    column_list = [c.name for c in Rooms.__table__.c]
    column_details_exclude_list = [Users.hashed_password]
    name = "Комната"
    name_plural = "Комнаты"
    icon = "fa-solid fa-user"


class HotelsAdmin(ModelView, model=Hotels):
    column_list = [c.name for c in Hotels.__table__.c]
    column_details_exclude_list = [Users.hashed_password]
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-user"
