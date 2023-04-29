from hotel.db.db_interface import DBInterface
from hotel.operations.models import (
    CustomerCreateData,
    CustomerResult,
    CustomerUpdateData,
)


def read_all_customers(customer_interface: DBInterface) -> list[CustomerResult]:
    return customer_interface.read_all()


def read_customer(customer_id: int, customer_interface: DBInterface) -> CustomerResult:
    return customer_interface.read_by_id(customer_id)


def create_customer(
    data: CustomerCreateData, customer_interface: DBInterface
) -> CustomerResult:
    return customer_interface.create(data)


def update_customer(
    customer_id: int, data: CustomerUpdateData, customer_interface: DBInterface
) -> CustomerResult:
    return customer_interface.update(customer_id, data)
