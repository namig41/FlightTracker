from fastapi import APIRouter, Depends, Request

from app.bookings.dao import BookingDAO

from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/moc_bookings.csv",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=user.id)


@router.get("/{booking_id}")
async def get_booking_by_id(booking_id: int):
    return await BookingDAO.find_or_one(id=booking_id)
