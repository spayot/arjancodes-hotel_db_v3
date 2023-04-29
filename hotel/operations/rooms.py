from hotel.db.db_interface import DBInterface
from hotel.operations.models import RoomResult


def read_all_rooms(room_interface: DBInterface) -> list[RoomResult]:
    return room_interface.read_all()


def read_room(room_id: int, room_interface: DBInterface) -> RoomResult:
    return room_interface.read_by_id(room_id)
