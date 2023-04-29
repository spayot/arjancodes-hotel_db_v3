from fastapi import APIRouter

from hotel.db.db_interface import DBInterface
from hotel.db.models import DBRoom
from hotel.operations.models import RoomResult
from hotel.operations.rooms import read_all_rooms, read_room

router = APIRouter()


@router.get("/rooms")
def api_read_all_rooms() -> list[RoomResult]:
    room_interface = DBInterface(DBRoom)
    return read_all_rooms(room_interface)


@router.get("/room/{room_id}")
def api_read_room(room_id: int) -> RoomResult:
    room_interface = DBInterface(DBRoom)
    return read_room(room_id, room_interface)
