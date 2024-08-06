from fastapi import APIRouter

from app.rooms.dao import RoomsDAO

router = APIRouter(
    prefix="/moc_rooms.csv",
    tags=["Комнаты"]
)


@router.get("")
async def get_rooms():
    return await RoomsDAO.find_by_id()

@router.get("/{room_id}")
async def get_room_by_id(room_id: int):
    return await RoomsDAO.find_by_id(room_id)
