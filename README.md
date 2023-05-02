# ArjanCodes - Software Designer Mindset - Extension - Hotel Booking API Challenge
## Description
This repo builds on top of the case study presented in [ArjanCodes' Software Designer Mindset course](https://www.arjancodes.com/products/the-software-designer-mindset-complete-extension/categories/2149106521). 
The case study ends by introducing a challenge to improve on the API design setup by Arjan. The following improvements have been performed:
* migrate `operations/customers` and `operations/rooms` to leverage the same `DBInterface` introduced by Arjan to reduce coupling for `bookings`.
* add a few fields to the customer database (address + consent to receive marketing email). i didn't go through the process of adding validation.
* create a new `/room_availability/v1` endpoint to query whether a room is available on a given time span or not.
* add room availability check before recording a booking (cf. [`_validate_room_availability`](hotel/operations/bookings.py))
* create a new `/available_rooms/v1` endpoint to retrieve all rooms available during a given time period.


## Interesting Implementation Details
### checking which rooms are available for a given timespan
- we choose to answer the question "which room is available?" by reframing it as **"which rooms don't have any booking overlapping wiht the time window of interest?"**. in more details:
- we retrieve the list of rooms by calling `room_interface.read_all()` (this could later on be extended to support additional filtering conditions, like amenity requirements, filtering on hotel, size, price, etc...)
- for each of those rooms, we determine whether at least one booking overlaps.
- the condition to identify overlapping bookings is: 
    - same `room_id` 
    - AND `booking(from_date)` < `query(to_date)` 
    - AND `booking(to_date)` > `query(from_date)`
- if there is no overlapping booking, then the room is available.

### extending DataInterface to handle filtering
* the `operations.DataInterface` has been extended to handle filtering.
* to keep it decoupled from sqlalchemy implementation details while maintaining good flexibility in the types of conditions supported, we define a `field_getter` method to the `DataInterface`. it returns a Callable that maps field names to a `Comparable` type of object. this `Comparable` object allows to compare individual fields to target values 
* example: 
```python
col = data_interface.field_getter()
data_interface.filter(
    (col("from_date") > "2023-01-01")
    & (col("room_id") == 3))
```
* this `field_getter` can be compared to the familiar `F.col` conveniently offered by `pyspark`.

## Open Questions
* would it be preferable to retrieve all bookings overlapping with time window, extract from them which rooms have been booked and return available rooms as the difference between all rooms and booked rooms? > seems like this would not as elegantly support extension to further filter rooms based on other properties...
* would it be preferable to add a new database table focused on room availability? what schema would be appropriate?
* is there a better way to extend the `DataInterface` and handle filtering?
* What is best practice for the API response to a binary question like: *is room 101 available between those dates?*
* what is the best way for the API to handle exceptions in a way that return something more informative than just `Internal Server Error`? (e.g. when trying to book a room that is not available)

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
You can find more examples of API queries in [doc/sample_curl_commands.sh](doc/sample_curl_commands.sh)

### Recording Booking
```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"room_id": 1, "customer_id": 4, "from_date": "2023-01-02", "to_date": "2023-01-03"}' \
http://localhost:8000/booking
```

### Retrieve all rooms available during a certain timespan
```bash
http://localhost:8000/available_rooms/v1?from_date=2023-01-15&to_date=2023-01-18
```
### Availability of a specific room
```
http://localhost:8000/room_availability/v1?room_id=1&from_date=2023-01-20&to_date=2023-01-26
```

# References
* https://www.arjancodes.com/products/the-software-designer-mindset-complete-extension/

