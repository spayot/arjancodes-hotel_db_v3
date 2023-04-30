import datetime as dt
from typing import Optional

from fastapi import APIRouter

from hotel.db.db_interface import DBInterface
from hotel.db.models import DBBooking, DBRoom
from hotel.operations.bookings import (
    create_booking,
    delete_booking,
    is_room_available,
    read_all_bookings,
    read_booking,
)
from hotel.operations.models import (
    BookingCreateData,
    BookingResult,
    RoomAvailabilityResult,
    RoomResult,
)

router = APIRouter()


@router.get("/bookings")
def api_read_all_bookings() -> list[BookingResult]:
    booking_interface = DBInterface(DBBooking)
    return read_all_bookings(booking_interface)


@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int) -> BookingResult:
    booking_interface = DBInterface(DBBooking)
    return read_booking(booking_id, booking_interface)


@router.post("/booking")
def api_create_booking(data: BookingCreateData):
    room_interface = DBInterface(DBRoom)
    booking_interface = DBInterface(DBBooking)
    return create_booking(data, room_interface, booking_interface)


@router.delete("/booking/{booking_id}")
def api_delete_booking(booking_id: int) -> BookingResult:
    booking_interface = DBInterface(DBBooking)
    return delete_booking(booking_id, booking_interface)


@router.get("/room_availability/v1")
def api_is_room_available(
    room_id: int, from_date: dt.date, to_date: Optional[dt.date] = None
) -> RoomAvailabilityResult:
    booking_interface = DBInterface(DBBooking)
    return is_room_available(room_id, from_date, to_date, booking_interface)
