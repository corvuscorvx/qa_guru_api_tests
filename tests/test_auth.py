import pytest
import requests
from jsonschema import validate
from typing import Any, Mapping

from schema.auth_schema import success_auth_schema, incorrect_data_schema, empty_fields_schema, unsupported_media_type

API_URL = "https://book-club.qa.guru/api/v1/auth/token/"
USERNAME = "qa_test_user_name"
PASSWORD = "1_qa_pas$"
TOKEN_PATH = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey"


def test_successful_auth():
    request_body = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(API_URL, json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, schema=success_auth_schema)

    access_token = body["access"]
    refresh_token = body["refresh"]
    assert TOKEN_PATH in access_token
    assert TOKEN_PATH in refresh_token
    assert len(access_token.split(".")) == 3
    assert len(refresh_token.split(".")) == 3
    assert access_token != refresh_token


def test_incorrect_password():
    request_body = {"username": USERNAME, "password": "incorrect"}

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 401

    body = response.json()
    validate(body, schema=incorrect_data_schema)

    assert body["detail"] == "Invalid username or password."


def test_incorrect_username():
    request_body = {"username": "incorrect", "password": PASSWORD}

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 401

    body = response.json()
    validate(body, schema=incorrect_data_schema)

    assert body["detail"] == "Invalid username or password."


def test_ignore_password():
    request_body = {"username": USERNAME}

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=empty_fields_schema)

    assert body["password"] == ["This field is required."]


def test_ignore_username():
    request_body = {"password": PASSWORD}

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=empty_fields_schema)

    assert body["username"] == ["This field is required."]


def test_ignore_username_and_password():
    request_body = {}

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=empty_fields_schema)

    assert body["username"] == ["This field is required."]
    assert body["password"] == ["This field is required."]


@pytest.mark.parametrize("username_type, password_type, expected_code, error_text, expected_schema", [
    pytest.param(None, None, 400, {"username": ["This field may not be null."], "password": ["This field may not be null."]}, empty_fields_schema),
    pytest.param(False, True, 400, {"username": ["Not a valid string."], "password": ["Not a valid string."]}, empty_fields_schema),
    pytest.param(50, 250, 401, {"detail": "Invalid username or password."}, incorrect_data_schema),
    pytest.param([], [], 400, {"username": ["Not a valid string."], "password": ["Not a valid string."]}, empty_fields_schema)
],
    ids=["type_None", "type_booleans", "type_integers", "type_lists"])
def test_incorrect_body_type_none(username_type, password_type, expected_code, error_text,
                                  expected_schema: Mapping[str, Any]):
    request_body = {
        "username": username_type,
        "password": password_type
    }

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.text)

    assert response.status_code == expected_code, f"Ожидали: {expected_code}, получили: {response.status_code}"

    body = response.json()
    validate(body, schema=expected_schema)

    assert body == error_text, f"Ожидали: {error_text}, получили: {body}"


def test_empty_username_and_password():
    request_body = {"username": "", "password": ""}

    response = requests.post(API_URL, json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 400

    body = response.json()
    validate(body, schema=empty_fields_schema)

    assert body["username"] == ["This field may not be blank."]
    assert body["password"] == ["This field may not be blank."]

def test_wrong_content_type_auth():
    request_body = {"username": USERNAME, "password": PASSWORD}
    headers = {"content-type": "image/png"}

    response = requests.post(API_URL, headers=headers, json=request_body)

    print("\nStatus code", response.status_code)
    print("Headers:", response.headers)
    print("Body", response.text)

    assert response.status_code == 415

    body = response.json()
    validate(body, schema=unsupported_media_type)

    assert body["detail"] == "Unsupported media type \"image/png\" in request."




