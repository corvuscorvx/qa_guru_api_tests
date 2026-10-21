import pytest
import requests

from faker import Faker
from jsonschema import validate
from schema.registration_schema import registration_schema, existing_registration_schema, empty_registration_schema

fake = Faker()
API_URL = "https://book-club.qa.guru/api/v1"
PASSWORD = f"test_pass_qwe"
USERNAME = f"test_name_qwe"


def test_correct_registration():
    request_body = {"username": fake.user_name(), "password": fake.password()}
    response = requests.post(f"{API_URL}/users/register/", json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 201

    body = response.json()
    validate(body, schema=registration_schema)

    assert body["username"] == request_body["username"]


def test_registration_with_existing_data():
    request_body = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(f"{API_URL}/users/register/", json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=existing_registration_schema)

    assert body["username"] == ["A user with that username already exists."]


@pytest.mark.parametrize("username, password, error_text", [
    pytest.param(None, None, {"username": ["This field may not be null."], "password": ["This field may not be null."]}),
    pytest.param("", "", {"username": ["This field may not be blank."], "password": ["This field may not be blank."]}),
    pytest.param(fake.user_name(), "", {"password": ["This field may not be blank."]}),
    pytest.param("", fake.password(), {"username": ["This field may not be blank."]}),
    pytest.param("    ", "     ", {"username": ["This field may not be blank."], "password": ["This field may not be blank."]})
],
    ids=["None_fields", "empty_fields", "empty_pass", "empty_name", "space_data"])
def test_registration_empty_fields(username, password, error_text):
    request_body = {"username": username, "password": password}

    response = requests.post(f"{API_URL}/users/register/", json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=empty_registration_schema)

    assert body == error_text


def test_registration_with_short_username():
    request_body = {"username": fake.user_name()[:1], "password": fake.password()}

    response = requests.post(f"{API_URL}/users/register/", json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 201

    body = response.json()
    validate(body, schema=registration_schema)

    assert body["username"] == request_body["username"]


def test_registration_with_long_username():
    request_body = {"username": fake.user_name()[:1] * 151, "password": "1"}
    response = requests.post(f"{API_URL}/users/register/", json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 400
    body = response.json()
    validate(body, schema=existing_registration_schema)

    assert body["username"] == ['Ensure this field has no more than 150 characters.']


def test_registration_with_long_password():
    request_body = {"username": fake.user_name(), "password": fake.password()[:1] * 129}
    response = requests.post(f"{API_URL}/users/register/", json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 400
    body = response.json()
    validate(body, schema=existing_registration_schema)

    assert body["password"] == ['Ensure this field has no more than 128 characters.']


def test_registration_invalid_username():
    request_body = {"username": "use! nam4", "password": fake.password()}
    response = requests.post(f"{API_URL}/users/register/", json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 400
    body = response.json()
    validate(body, schema=existing_registration_schema)

    assert body["username"] == ["Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters."]
