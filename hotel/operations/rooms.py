import datetime as dt

from hotel.operations.bookings import _is_room_available_during_timespan
from hotel.operations.interface import DataInterface
from hotel.operations.models import RoomResult


def read_all_rooms(room_interface: DataInterface) -> list[RoomResult]:
    return room_interface.read_all()


def read_room(room_id: int, room_interface: DataInterface) -> RoomResult:
    return room_interface.read_by_id(room_id)


def search_available_rooms(
    from_date: dt.date, to_date: dt.date, room_interface: DataInterface
) -> list[RoomResult]:
    all_rooms: list[RoomResult] = room_interface.read_all()
    return [
        room
        for room in all_rooms
        if _is_room_available_during_timespan(room["id"], from_date, to_date)
    ]
