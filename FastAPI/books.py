# pylint: disable=missing-docstring
# pylint: disable=invalid-name

from fastapi import FastAPI
from  enum import Enum
from typing import Optional

app = FastAPI()

BOOKS = {
    'book_1' : {"title": "Title one", "author" : "Author One"},
    'book_2' : {"title": "Title two", "author" : "Author Two"},
    'book_3' : {"title": "Title three", "author" : "Author Three"},
    'book_4' : {"title": "Title four", "author" : "Author Four"},
    'book_5' : {"title": "Title five", "author" : "Author Five"}
}

class DirectionName(str, Enum):
    north = "North"
    east = "East"
    south = "South"
    west = "West"



@app.get("/")
async def read_all_books(skip_book : Optional[str] = None):
    if skip_book:
        new_book = BOOKS.copy()
        del new_book[skip_book]
        return new_book
    return BOOKS

@app.get("/{book_name}")
async def read_book(book_name : str):
    return BOOKS[book_name]

@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0
    if len(BOOKS)>0:
        for book in BOOKS:
            x = int(book.split("_")[-1])
            if x > current_book_id:
                current_book_id = x
    BOOKS[f"book_{current_book_id+1}"] = {"book_title":  book_title,"book_author": book_author}
    return BOOKS[f"book_{current_book_id+1}"]


@app.put("/{book_name}")
async def update_book(book_name,book_title,book_author):
    BOOKS[book_name] = {"book_title": book_title, "book_author" : book_author}
    #BOOKS[f"book_{book_id}"] = {"book_title": book_title, "book_author" : book_author}
    return BOOKS[book_name]


@app.delete("/{book_name}")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f"{book_name} deleted"

#create read_book and delete_book using query parameters
#instead of path parameters
@app.get("/assignment/")
async def read_book_q(book_name :str):
    return BOOKS[book_name]

@app.delete("/assignment/")
async def delete_book_q(book_name : str):
    del BOOKS[book_name]
    return f"{book_name} deleted"


# this app endpoint use the same path as the one with parameters 
# hence it should always preceed it to avoid validation errors
@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title" : "My favorite book"}

@app.get("/books/{book_id}")
async def read_book(book_id:int):
    return {"book_title" : book_id}


@app.get("/directions/{direction_name}")
async def get_direction(direction_name : DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub" : "Up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub" : "Down"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub" : "Left"}
    return {"Direction": direction_name, "sub" : "Right"}


