"""
Employee class tests.
"""
import unittest
from datetime import date

from hotel.db.db_interface import DataObject
from hotel.operations.models import RoomAvailabilityResult
from hotel.operations.rooms import check_room_availability


def main():
    print(check_room_availability(1, date(2023, 1, 10)))


if __name__ == "__main__":
    main()
