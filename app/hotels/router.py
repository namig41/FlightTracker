import asyncio

from fastapi import APIRouter

from app.hotels.dao import HotelsDAO
from fastapi_cache.decorator import cache


router = APIRouter(
    prefix="/moc_hotels.csv",
    tags=["Отели"]
)


@router.get("")
@cache(expire=20)
async def get_hotels():
    await asyncio.sleep(10)
    return await HotelsDAO.find_all()


@router.get("/{hotel_id}")
async def get_hotel_by_id(hotel_id: int):
    return await HotelsDAO.find_by_id(hotel_id)
