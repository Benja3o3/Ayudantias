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
    response = client.post("/authors", json={"id": 1, "name": "Author 1", "birth_year": 1970})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Author 1", "birth_year": 1971}

def test_get_authors():
    client.post("/authors", json={"id": 1, "name": "Author 1", "birth_year": 1970})
    response = client.get("/authors")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Author 1", "birth_year": 1970}]

def test_get_author():
    client.post("/authors", json={"id": 1, "name": "Author 1", "birth_year": 1970})
    response = client.get("/authors/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Author 1", "birth_year": 1970}

def test_update_author():
    client.post("/authors", json={"id": 1, "name": "Author 1", "birth_year": 1970})
    response = client.put("/authors/1", json={"id": 1, "name": "Updated Author", "birth_year": 1971})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Updated Author", "birth_year": 1971}

def test_delete_author():
    client.post("/authors", json={"id": 1, "name": "Author 1", "birth_year": 1970})
    response = client.delete("/authors/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Author deleted successfully"}
    response = client.get("/authors/1")
    assert response.status_code == 404

def test_create_book():
    client.post("/authors", json={"id": 2, "name": "Author 2", "birth_year": 1980})
    response = client.post("/books", json={"id": 1, "title": "Book 1", "author_id": 2, "year": 2000})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Book 1", "author_id": 2, "year": 2000}

def test_get_books():
    client.post("/authors", json={"id": 2, "name": "Author 2", "birth_year": 1980})
    client.post("/books", json={"id": 1, "title": "Book 1", "author_id": 2, "year": 2000})
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "title": "Book 1", "author_id": 2, "year": 2000}]

def test_get_book():
    client.post("/authors", json={"id": 2, "name": "Author 2", "birth_year": 1980})
    client.post("/books", json={"id": 1, "title": "Book 1", "author_id": 2, "year": 2000})
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Book 1", "author_id": 2, "year": 2000}

def test_update_book():
    client.post("/authors", json={"id": 2, "name": "Author 2", "birth_year": 1980})
    client.post("/books", json={"id": 1, "title": "Book 1", "author_id": 2, "year": 2000})
    response = client.put("/books/1", json={"id": 1, "title": "Updated Book", "author_id": 2, "year": 2001})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Updated Book", "author_id": 2, "year": 2001}

def test_delete_book():
    client.post("/authors", json={"id": 2, "name": "Author 2", "birth_year": 1980})
    client.post("/books", json={"id": 1, "title": "Book 1", "author_id": 2, "year": 2000})
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted successfully"}
    response = client.get("/books/1")
    assert response.status_code == 404

if __name__ == "__main__":
    # Ejecución de las pruebas
    pytest.main()