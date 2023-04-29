from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base
from .sample_data import bookings, customers, rooms


def create_db(file: str):
    engine = create_engine(file)
    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Insert a few customers into the customers table
    session.add_all(customers)

    # Insert a few rooms into the rooms table
    session.add_all(rooms)

    # insert a few bookings into the bookings table
    session.add_all(bookings)
    session.commit()
