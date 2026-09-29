import requests
from jsonschema import validate
from schema.schema_search import search_fore_title_schema
from schema.schema_search import search_fore_author_schema
from schema.schema_page_size import page_size_shema

BASE_URL = 'https://book-club.qa.guru'
endpoint = '/api/v1/clubs/'


def test_search_fore_title():
    title = {"search": "GURU-QA The Wives of Bath"}
    response = requests.get(BASE_URL + endpoint, title)

    print("\nStatus code", response.status_code)
    print("Body", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, search_fore_title_schema)

    assert body["results"][0]["bookTitle"] == "GURU-QA The Wives of Bath"
    print(f"Ожидали 'GURU-QA The Wives of Bath', а пришло {body['results'][0]['bookTitle']}")


def test_search_for_author():
    author = {"search": "Garrett Bahringer"}
    response = requests.get(BASE_URL + endpoint, author)

    print("\nStatus code", response.status_code)
    print("Body", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, search_fore_author_schema)

    assert body["count"] == 0
    print(f"Ожидали 0 результатов, а пришло {body['count']}")
    assert len(body["results"]) == 0
    print("Пришел пустйо массив")


def test_pagination_page():
    page_number = {"page": 6}
    response = requests.get(BASE_URL + endpoint, page_number)

    print("\nStatus code", response.status_code)
    print("Body", response.text)

    assert response.status_code == 200

    body = response.json()

    assert "page=5" in body["previous"]
    print(f"Ожидали в previous страницу 5, а получили: {body['previous']}")

    assert "page=7" in body["next"]
    print(f"Ожидали in next страницу 7, а получили: {body['next']}")


def test_page_size():
    count = {"page_size": 10}
    response = requests.get(BASE_URL + endpoint, count)

    print("\nStatus code", response.status_code)
    print("Body", response.text)

    assert response.status_code == 200

    body = response.json()
    validate(body, page_size_shema)

    actual_page_size = 10
    assert len(body["results"]) == actual_page_size
    print(f"Ожидали {actual_page_size} книг на странице, а получили {len(body['results'])}")
