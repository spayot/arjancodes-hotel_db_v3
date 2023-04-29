# ArjanCodes - Software Designer Mindset - Extension - Hotel Booking API
## Description
This repo builds on top of the case study presented in [ArjanCodes' Software Designer Mindset course](https://www.arjancodes.com/products/the-software-designer-mindset-complete-extension/categories/2149106521). 
The case study by introducing a challenge to improve on the API as setup by Arjan. The following improvements have been performed:
* migrate `operations/customers` and `operations/rooms` to leverage the same `DBInterface` introduced to reduce coupling for `bookings`.
* add a few fields to the customer database (address + consent to receive marketing email)
* create a new `/room_availability/v1` endpoint to query whether a room is available on a given time span.

## Installing and running the hotel reservation API example

To make running the case study easy, you can install poetry to handle the dependencies. You can install poetry by running:

```bash
pip install poetry
```

Then, you can install the dependencies by running:

```bash
poetry install
```

To start the API server, run the following command:

```bash
poetry run uvicorn main:app --reload
```

## Querying the API endpoints
### Recording Booking
```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"room_id": 1, "customer_id": 4, "from_date": "2023-01-02", "to_date": "2023-01-03"}' \
http://localhost:8000/booking
```

### Room Availability
```
http://localhost:8000/room_availability/v1?room_id=1&from_date=2023-01-20&to_date=2023-01-26
```