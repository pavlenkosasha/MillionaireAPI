import requests

response = requests.post(
    "http://127.0.0.1:5000/answer",
    json={
        "id": 2,
        "answer": "7"
    }
)

print(response.json())