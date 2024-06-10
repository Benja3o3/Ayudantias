from fastapi import FastAPI, HTTPException
from models import Author, Book
from typing import List
import json
import os

app = FastAPI()

# Rutas de los archivos JSON
BOOKS_FILE = 'books.json'
AUTHORS_FILE = 'authors.json'



# Funciones auxiliares para manejar archivos JSON
def load_data(file_path: str):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def save_data(file_path: str, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Cargar datos al iniciar la aplicación
authors_db = load_data(AUTHORS_FILE)
books_db = load_data(BOOKS_FILE)

# Rutas para autores
@app.get("/authors", response_model=List[Author])
def get_authors():
    return authors_db

@app.get("/authors/{author_id}", response_model=Author)
def get_author(author_id: int):
    for author in authors_db:
        if author["id"] == author_id:
            return author
    raise HTTPException(status_code=404, detail="Author not found")

@app.post("/authors", response_model=Author)
def create_author(author: Author):
    for a in authors_db:
        if a["id"] == author.id:
            raise HTTPException(status_code=400, detail="Author with this ID already exists")
    authors_db.append(author.model_dump())
    save_data(AUTHORS_FILE, authors_db)
    return author

@app.put("/authors/{author_id}", response_model=Author)
def update_author(author_id: int, updated_author: Author):
    for index, author in enumerate(authors_db):
        if author["id"] == author_id:
            authors_db[index] = updated_author.model_dump()
            save_data(AUTHORS_FILE, authors_db)
            return updated_author
    raise HTTPException(status_code=404, detail="Author not found")

@app.delete("/authors/{author_id}")
def delete_author(author_id: int):
    for index, author in enumerate(authors_db):
        if author["id"] == author_id:
            del authors_db[index]
            save_data(AUTHORS_FILE, authors_db)
            return {"message": "Author deleted successfully"}
    raise HTTPException(status_code=404, detail="Author not found")

# Rutas para libros
@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def create_book(book: Book):
    for b in books_db:
        if b["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    for author in authors_db:
        if author["id"] == book.author_id:
            books_db.append(book.model_dump())
            save_data(BOOKS_FILE, books_db)
            return book
    raise HTTPException(status_code=400, detail="Author ID not found")

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book["id"] == book_id:
            for author in authors_db:
                if author["id"] == updated_book.author_id:
                    books_db[index] = updated_book.model_dump()
                    save_data(BOOKS_FILE, books_db)
                    return updated_book
            raise HTTPException(status_code=400, detail="Author ID not found")
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book["id"] == book_id:
            del books_db[index]
            save_data(BOOKS_FILE, books_db)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
