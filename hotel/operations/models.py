import datetime as dt
from typing import Optional

from pydantic import BaseModel


class CustomerCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    address_street: Optional[str]
    address_city: Optional[str]
    address_zip: Optional[int]
    accepts_marketing_emails: bool = False


class CustomerUpdateData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: Optional[str]
    address_street: Optional[str]
    address_city: Optional[str]
    address_zip: Optional[int]


class BookingCreateData(BaseModel):
    room_id: int
    customer_id: int
    from_date: dt.date
    to_date: dt.date


class BookingResult(BaseModel):
    id: int
    room_id: int
    customer_id: int
    price: int
    from_date: dt.date
    to_date: dt.date


class CustomerResult(BaseModel):
    id: int
    first_name: str
    last_name: str
    email_address: str
    address_street: Optional[str]
    address_city: Optional[str]
    address_zip: Optional[int]
    accepts_marketing_emails: bool = False


class RoomResult(BaseModel):
    id: int
    number: str
    size: int
    price: int


class RoomAvailabilityResult(BaseModel):
    room_id: int
    from_date: dt.date
    to_date: dt.date
    is_available: bool
