from datetime import date
from pydantic import BaseModel
from sqlalchemy import JSON


class SBooking(BaseModel):
    room_id: int
    location: str
    services: JSON
    date_to: date
    date_from: date
    stars: int
    rooms_quantity: int