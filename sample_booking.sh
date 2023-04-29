curl -X POST \
-H "Content-Type: application/json" \
-d '{"room_id": 1, "customer_id": 2, "from_date": "2023-01-01", "to_date": "2023-01-20"}' \
http://localhost:8000/booking

curl -X POST \
-H "Content-Type: application/json" \
-d '{"room_id": 1, "customer_id": 1, "from_date": "2023-01-25", "to_date": "2023-01-30"}' \
http://localhost:8000/booking

curl -X POST \
-H "Content-Type: application/json" \
-d '{"room_id": 2, "customer_id": 3, "from_date": "2023-01-01", "to_date": "2023-01-10"}' \
http://localhost:8000/booking

# testing availability validation: should return Internal Server Error
curl -X POST \
-H "Content-Type: application/json" \
-d '{"room_id": 1, "customer_id": 4, "from_date": "2023-01-02", "to_date": "2023-01-03"}' \
http://localhost:8000/booking