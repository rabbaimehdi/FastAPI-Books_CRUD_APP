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

