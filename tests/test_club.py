import requests
import random
import pytest

from typing import Any, Mapping
from jsonschema import validate
from faker import Faker
from schema.club_schema import create_success_club_schema, create_club_without_authorization, \
    create_club_without_invalid_access_token_schema, create_empty_telegram_schema, \
    create_empty_description_schema, create_empty_year_schema, create_empty_author_schema, create_empty_title_schema, \
    update_club_schema

fake = Faker()
API_URL = "https://book-club.qa.guru/api/v1"
USERNAME = "test_name_qwe"
PASSWORD = "test_pass_qwe"
USER_ID = 10366


def test_success_create_club():
    auth_body = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(f"{API_URL}/auth/token/", json=auth_body)
    access_token = response.json()["access"]

    book_title = fake.catch_phrase()
    book_authors = fake.name()
    public_year = random.randint(1800, 2026)
    description = fake.sentence()

    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": public_year,
        "description": description,
        "telegramChatLink": "https://t.me/qa-guru"
    }
    club_headers = {"Authorization": "Bearer " + access_token}
    club_response = requests.post(f"{API_URL}/clubs/", headers=club_headers, json=club_body)

    print("\nStatus code", club_response.status_code)
    print("Headers:", club_response.headers)
    print("Body", club_response.text)

    assert club_response.status_code == 201

    club_response_body = club_response.json()
    validate(club_response_body, schema=create_success_club_schema)

    assert club_response_body["bookTitle"] == book_title
    assert club_response_body["bookAuthors"] == book_authors
    assert club_response_body["publicationYear"] == public_year
    assert club_response_body["description"] == description
    assert club_response_body["telegramChatLink"] == "https://t.me/qa-guru"
    assert club_response_body["owner"] == USER_ID
    assert USER_ID in club_response_body["members"]
    assert club_response_body["modified"] is None

def test_update_club():
    auth_body = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(f"{API_URL}/auth/token/", json=auth_body)
    access_token = response.json()["access"]

    book_title = fake.catch_phrase()
    book_authors = fake.name()
    public_year = random.randint(1800, 2026)
    description = fake.sentence()

    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": public_year,
        "description": description,
        "telegramChatLink": "https://t.me/qa-guru"
    }

    club_headers = {"Authorization": "Bearer " + access_token}
    club_response = requests.post(f"{API_URL}/clubs/", headers=club_headers, json=club_body)
    club_id = str(club_response.json()["id"])

    new_book_title = fake.catch_phrase()
    new_book_authors = fake.name()
    new_public_year = random.randint(1800, 2026)
    new_description = fake.sentence()

    new_club_body = {
        "bookTitle": new_book_title,
        "bookAuthors": new_book_authors,
        "publicationYear": new_public_year,
        "description": new_description,
        "telegramChatLink": "https://t.me/qa-guru-new"
    }
    new_club_headers = {"Authorization": "Bearer " + access_token}
    put_response = requests.put(API_URL + "/clubs/" + club_id + "/", headers=new_club_headers, json=new_club_body)

    print("\nStatus code: ", put_response.status_code)
    print("Headers: ", put_response.headers)
    print("Body: ", put_response.text)

    body = put_response.json()
    validate(body, schema=update_club_schema)

    assert put_response.status_code == 200
    assert body["bookTitle"] == new_club_body["bookTitle"]
    assert body["bookAuthors"] == new_club_body["bookAuthors"]
    assert body["publicationYear"] == new_club_body["publicationYear"]
    assert body["description"] == new_club_body["description"]
    assert body["telegramChatLink"] == new_club_body["telegramChatLink"]
    assert body["modified"] is not None



@pytest.mark.parametrize("data, error_field, error_text, schema", [
    pytest.param({"title": fake.catch_phrase(), "author": fake.name(), "year": random.randint(1800, 2026), "description": fake.sentence(), "link": ""}, "telegramChatLink", ["This field may not be blank."], create_empty_telegram_schema),
    pytest.param({"title": fake.catch_phrase(), "author": fake.name(), "year": random.randint(1800, 2026), "description": "", "link": "https://t.me/qa-guru"}, "description", ["This field may not be blank."], create_empty_description_schema),
    pytest.param({"title": fake.catch_phrase(), "author": fake.name(), "year": "", "description": fake.sentence(), "link": "https://t.me/qa-guru"}, "publicationYear", ["A valid integer is required."], create_empty_year_schema),
    pytest.param({"title": fake.catch_phrase(), "author": "", "year": random.randint(1800, 2026), "description": fake.sentence(), "link": "https://t.me/qa-guru"}, "bookAuthors", ["This field may not be blank."], create_empty_author_schema),
    pytest.param({"title": "", "author": fake.name(), "year": random.randint(1800, 2026), "description": fake.sentence(), "link": "https://t.me/qa-guru"}, "bookTitle", ["This field may not be blank."], create_empty_title_schema)
],
    ids=["empty_link", "empty_description", "empty_year", "empty_author", "empty_title"])
def test_create_club_with_empty_fields(data, error_field, error_text, schema: Mapping[str, Any]):
    auth_body = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(f"{API_URL}/auth/token/", json=auth_body)
    access_token = response.json()["access"]

    club_body = {
        "bookTitle": data["title"],
        "bookAuthors": data["author"],
        "publicationYear": data["year"],
        "description": data["description"],
        "telegramChatLink": data["link"]
    }
    club_headers = {"Authorization": "Bearer " + access_token}
    club_response = requests.post(f"{API_URL}/clubs/", headers=club_headers, json=club_body)

    print("\nStatus code", club_response.status_code)
    print("Headers:", club_response.headers)
    print("Body", club_response.text)

    assert club_response.status_code == 400

    club_response_body = club_response.json()
    validate(club_response_body, schema=schema)

    assert club_response_body[error_field] == error_text


def test_create_club_without_authorization():
    book_title = fake.catch_phrase()
    book_authors = fake.name()
    public_year = random.randint(1800, 2026)
    description = fake.sentence()

    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": public_year,
        "description": description,
        "telegramChatLink": "https://t.me/qa-guru"
    }
    club_response = requests.post(f"{API_URL}/clubs/", json=club_body)

    print("\nStatus code", club_response.status_code)
    print("Headers:", club_response.headers)
    print("Body", club_response.text)

    assert club_response.status_code == 401

    club_response_body = club_response.json()
    validate(club_response_body, schema=create_club_without_authorization)

    assert club_response_body["detail"] == "Authentication credentials were not provided."


def test_create_club_with_invalid_access_token():
    invalid_access_token = "Bearer l90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkzMTgzMzQxLCJpY"

    book_title = fake.catch_phrase()
    book_authors = fake.name()
    public_year = random.randint(1800, 2026)
    description = fake.sentence()

    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": public_year,
        "description": description,
        "telegramChatLink": "https://t.me/qa-guru"
    }
    club_headers = {"Authorization": invalid_access_token}
    club_response = requests.post(f"{API_URL}/clubs/", headers=club_headers, json=club_body)

    print("\nStatus code", club_response.status_code)
    print("Headers:", club_response.headers)
    print("Body", club_response.text)

    assert club_response.status_code == 401

    club_response_body = club_response.json()
    validate(club_response_body, schema=create_club_without_invalid_access_token_schema)

    assert club_response_body["detail"] == "Given token not valid for any token type"
    assert club_response_body["code"] == "token_not_valid"
    assert club_response_body["messages"][0]["message"] == "Token is invalid"


def test_success_delete_club():
    auth_body = {"username": USERNAME, "password": PASSWORD}
    response = requests.post(f"{API_URL}/auth/token/", json=auth_body)
    access_token = response.json()["access"]

    book_title = fake.catch_phrase()
    book_authors = fake.name()
    public_year = random.randint(1800, 2026)
    description = fake.sentence()

    club_body = {
        "bookTitle": book_title,
        "bookAuthors": book_authors,
        "publicationYear": public_year,
        "description": description,
        "telegramChatLink": "https://t.me/qa-guru"
    }

    club_headers = {"Authorization": "Bearer " + access_token}
    club_response = requests.post(f"{API_URL}/clubs/", headers=club_headers, json=club_body)
    club_id = str(club_response.json()["id"])

    delete_response = requests.delete(API_URL + "/clubs/" + club_id, headers=club_headers)

    assert delete_response.status_code == 204
