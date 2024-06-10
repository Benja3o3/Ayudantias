import pytest
from fastapi.testclient import TestClient
from api import app, authors_db, books_db, AUTHORS_FILE, BOOKS_FILE

client = TestClient(app)


# Limpieza de bases de datos para pruebas
@pytest.fixture(autouse=True)
def setup_and_teardown():
    authors_db.clear()
    books_db.clear()
    yield
    authors_db.clear()
    books_db.clear()


def test_create_author():
    response = client.post(
        "/authors", json={"id": 1, "name": "Author 1", "birth_year": 1970}
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Author 1", "birth_year": 1970}


def test_get_authors():
    client.post("/authors", json={"id": 1, "name": "Author 1", "birth_year": 1970})
    response = client.get("/authors")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Author 1", "birth_year": 1970}]


if __name__ == "__main__":
    # Ejecución de las pruebas
    pytest.main()
