from fastapi import APIRouter

from hotel.db.db_interface import DBInterface
from hotel.db.models import DBCustomer
from hotel.operations.customers import (
    create_customer,
    read_all_customers,
    read_customer,
    update_customer,
)
from hotel.operations.models import (
    CustomerCreateData,
    CustomerResult,
    CustomerUpdateData,
)

router = APIRouter()


@router.get("/customers")
def api_read_all_customers() -> list[CustomerResult]:
    customer_interface = DBInterface(DBCustomer)
    return read_all_customers(customer_interface)


@router.get("/customer/{customer_id}")
def api_read_customer(customer_id: int) -> CustomerResult:
    customer_interface = DBInterface(DBCustomer)
    return read_customer(customer_id, customer_interface)


@router.post("/customer")
def api_create_customer(customer: CustomerCreateData) -> CustomerResult:
    customer_interface = DBInterface(DBCustomer)
    return create_customer(customer, customer_interface)


@router.post("/customer/{customer_id}")
def api_update_customer(
    customer_id: int, customer: CustomerUpdateData
) -> CustomerResult:
    customer_interface = DBInterface(DBCustomer)
    return update_customer(customer_id, customer, customer_interface)
