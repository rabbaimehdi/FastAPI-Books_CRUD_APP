# pylint: disable=missing-docstring

from fastapi import FastAPI

BOOKS = {
    'book_1' : {"title": "Title one", "author" : "Author One"},
    'book_2' : {"title": "Title two", "author" : "Author Two"},
    'book_3' : {"title": "Title three", "author" : "Author Three"},
    'book_4' : {"title": "Title four", "author" : "Author Four"},
    'book_5' : {"title": "Title five", "author" : "Author Five"}
}
app = FastAPI()
@app.get("/")
async def read_all_books():
    return BOOKS

# this app endpoint use the same path as the one with parameters 
# hence it should always preceed it to avoid validation errors
@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title" : "My favorite book"}

@app.get("/books/{book_id}")
async def read_book(book_id:int):
    return {"book_title" : book_id}


