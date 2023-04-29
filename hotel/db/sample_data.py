from hotel.db.models import DBBooking, DBCustomer, DBRoom

customers = [
    DBCustomer(
        first_name="John",
        last_name="Smith",
        email_address="email@email.com",
        address_street="123, John Doe Street",
        address_city="Portland",
        address_zip=12345,
        accepts_marketing_emails=True,
    ),
    DBCustomer(
        first_name="Jane",
        last_name="Doe",
        email_address="jane@hotmail.com",
        address_street="456, Sesame Avenue",
        address_city="Seattle",
        address_zip=67890,
        accepts_marketing_emails=False,
    ),
    DBCustomer(
        first_name="Jack",
        last_name="Black",
        email_address="jack@black.com",
        address_street="222, Main Street",
        address_city="Springfield",
        address_zip=11111,
        accepts_marketing_emails=True,
    ),
    DBCustomer(
        first_name="Jill",
        last_name="White",
        email_address="jill@gmail.com",
        accepts_marketing_emails=True,
    ),
    DBCustomer(
        first_name="Arjan",
        last_name="Codes",
        email_address="hi@arjancodes.com",
        address_street="901, Utrecht Strasse",
        address_city="Amsterdam",
        address_zip=1234,
        accepts_marketing_emails=True,
    ),
]

rooms = [
    DBRoom(number="101", size=10, price=150_00),
    DBRoom(number="102", size=10, price=150_00),
    DBRoom(number="103", size=20, price=250_00),
    DBRoom(number="104", size=20, price=250_00),
    DBRoom(number="105", size=30, price=350_00),
]
