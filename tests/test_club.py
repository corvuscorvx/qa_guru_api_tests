import requests
from jsonschema import validate
import random
from schema.club_schema import success_create_club_schema

API_URL = "https://book-club.qa.guru/api/v1"
USERNAME = "qa_test_user_name"
PASSWORD = "1_qa_pas$"

def test_success_create_club():
    auth_body = {"username": USERNAME, "password": PASSWORD}
    auth_response = requests.post(API_URL + "/auth/token/", json=auth_body)
    access_token = auth_response.json()["access"]

    book_title = f"random_book {random.randint(10000, 99999)}"
    book_author = f"random_author {random.randint(10000, 99999)}"
    publication_year = random.randint(2140000000, 2149999999)
    club_body = {
      "bookTitle": book_title,
      "bookAuthors": book_author,
      "publicationYear": publication_year,
      "description": "string",
      "telegramChatLink": "https://t.me/qa.guru"
    }
    club_headers = {"Authorization": "Bearer " + access_token}
    club_response = requests.post(API_URL + "/clubs/", headers=club_headers, json=club_body)

    print("\nStatus code", club_response.status_code)
    print("Headers:", club_response.headers)
    print("Body", club_response.text)

    assert club_response.status_code == 201

    club_response_body = club_response.json()
    validate(club_response_body, schema=success_create_club_schema)

    assert club_response_body["bookTitle"] == book_title
    assert club_response_body["bookAuthors"] == book_author