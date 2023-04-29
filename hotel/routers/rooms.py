import datetime as dt

from fastapi import APIRouter

from hotel.db.db_interface import DBInterface
from hotel.db.models import DBRoom
from hotel.operations.models import RoomResult
from hotel.operations.rooms import read_all_rooms, read_room, search_available_rooms

router = APIRouter()


@router.get("/rooms")
def api_read_all_rooms() -> list[RoomResult]:
    room_interface = DBInterface(DBRoom)
    return read_all_rooms(room_interface)


@router.get("/room/{room_id}")
def api_read_room(room_id: int) -> RoomResult:
    room_interface = DBInterface(DBRoom)
    return read_room(room_id, room_interface)


@router.get("/available_rooms/v1")
def api_search_available_rooms(
    from_date: dt.date, to_date: dt.date
) -> list[RoomResult]:
    room_interface = DBInterface(DBRoom)
    return search_available_rooms(from_date, to_date, room_interface)
