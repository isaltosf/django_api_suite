import requests
import json

url = "http://127.0.0.1:8000/landing/api/index/"
headers = {"Content-Type": "application/json"}
data = {
    "name": "Test User",
    "email": "test@example.com",
    "message": "Hello world"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
except Exception as e:
    print(f"Error: {e}")
