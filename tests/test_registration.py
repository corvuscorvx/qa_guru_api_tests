import uuid
import requests

from jsonschema import validate

from schema.registration_schema import registration_schema

API_URL = "https://book-club.qa.guru/api/v1"
PASSWORD = "1q_test$_pa551"


def test_correct_registration():
    username = f"test_user_{uuid.uuid4().hex[:6]}"
    request_body = {"username": username, "password": PASSWORD}
    response = requests.post(f"{API_URL}/users/register/", json=request_body)
    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 201

    body = response.json()
    validate(body, schema=registration_schema)

    assert body["username"] == request_body["username"]

    response_auth = requests.post(f"{API_URL}/auth/token/", json=request_body)
    print("\nStatus code", response_auth.status_code)

    assert response_auth.status_code == 200

    token = response_auth.json()["access"]
    headers = {"Authorization": f"Bearer {token}"}
    response_delete = requests.delete(f"{API_URL}/users/me/", headers=headers)
    print("\nStatus code", response_delete.status_code)
    print("Headers:", response_delete.headers)
    print("Body", response_delete.text)
    assert response_delete.status_code == 204
