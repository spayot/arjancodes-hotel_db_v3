import datetime as dt
from typing import Optional, Union

from hotel.db.engine import DBSession
from hotel.db.models import DBBooking
from hotel.operations.interface import DataInterface
from hotel.operations.models import (
    BookingCreateData,
    BookingResult,
    RoomAvailabilityResult,
    RoomResult,
)


def read_all_bookings(booking_interface: DataInterface) -> list[BookingResult]:
    bookings = booking_interface.read_all()
    return [BookingResult(**b) for b in bookings]


def read_booking(booking_id: int, booking_interface: DataInterface) -> BookingResult:
    booking = booking_interface.read_by_id(booking_id)
    return BookingResult(**booking)


def create_booking(
    data: BookingCreateData,
    room_interface: DataInterface,
    booking_interface: DataInterface,
) -> BookingResult:

    # retrieve the room
    room = room_interface.read_by_id(data.room_id)

    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise ValueError("Invalid dates")

    _validate_room_availability(data.room_id, data.from_date, data.to_date)

    booking_dict = data.dict()
    booking_dict["price"] = room["price"] * days

    booking = booking_interface.create(booking_dict)
    return BookingResult(**booking)


def _validate_room_availability(
    room_id: int, from_date: dt.date, to_date: dt.date
) -> None:
    room_availability_result = is_room_available(room_id, from_date, to_date)
    if not room_availability_result.is_available:
        raise ValueError(f"Room not available")


def delete_booking(booking_id: int, booking_interface: DataInterface) -> BookingResult:
    booking = booking_interface.delete(booking_id)
    return BookingResult(**booking)


def is_room_available(
    room_id: int, from_date: dt.date, to_date: Optional[dt.date]
) -> RoomAvailabilityResult:
    if not to_date:
        to_date = dt.datetime.strptime(from_date, "%Y-%m-%d").date() + dt.timedelta(
            days=1
        )

    is_available: bool = _is_room_available_during_timespan(room_id, from_date, to_date)

    return RoomAvailabilityResult(
        room_id=room_id,
        from_date=from_date,
        to_date=to_date,
        is_available=is_available,
    )


def _is_room_available_during_timespan(
    room_id: int, from_date: dt.date, to_date: Optional[dt.date]
) -> bool:
    bookings = _retrieve_room_bookings_during_timespan(room_id, from_date, to_date)
    return not bookings


def _retrieve_room_bookings_during_timespan(
    room_id: int, from_date: dt.date, to_date: dt.date
) -> list[DBBooking]:

    session = DBSession()
    bookings: list[DBBooking] = (
        session.query(DBBooking)
        .filter(DBBooking.room_id == room_id)
        .filter((DBBooking.from_date < to_date) & (DBBooking.to_date > from_date))
        .all()
    )
    session.close()
    return bookings


def search_available_rooms(
    from_date: dt.date, to_date: dt.date, room_interface: DataInterface
) -> list[RoomResult]:
    all_rooms: list[RoomResult] = room_interface.read_all()
    return [
        room
        for room in all_rooms
        if _is_room_available_during_timespan(room["id"], from_date, to_date)
    ]
