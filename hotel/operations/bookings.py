import datetime as dt
from typing import Any, Optional

from hotel.db.models import DBBooking
from hotel.operations.interface import DataInterface
from hotel.operations.models import (
    BookingCreateData,
    BookingResult,
    RoomAvailabilityResult,
)

DataObject = dict[str, Any]


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
    room_id: int,
    from_date: dt.date,
    to_date: Optional[dt.date],
    booking_interface: DataInterface,
) -> RoomAvailabilityResult:
    if not to_date:
        to_date = dt.datetime.strptime(from_date, "%Y-%m-%d").date() + dt.timedelta(
            days=1
        )

    bookings_during_timespan = _retrieve_room_bookings_during_timespan(
        room_id, from_date, to_date, booking_interface
    )

    return RoomAvailabilityResult(
        room_id=room_id,
        from_date=from_date,
        to_date=to_date,
        is_available=not bookings_during_timespan,
    )


def _retrieve_room_bookings_during_timespan(
    room_id: int, from_date: dt.date, to_date: dt.date, booking_interface: DataInterface
) -> list[DataObject]:
    condition = (
        (DBBooking.room_id == room_id)
        & (DBBooking.from_date < to_date)
        & (DBBooking.to_date > from_date)
    )
    print(type(condition))
    return booking_interface.filter(condition)
