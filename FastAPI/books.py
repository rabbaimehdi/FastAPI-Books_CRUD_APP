# pylint: disable=missing-docstring
# pylint: disable=invalid-name

from fastapi import FastAPI
from  enum import Enum

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


@app.get("/directions/{direction_name}")
async def get_direction(direction_name : DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub" : "Up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub" : "Down"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub" : "Left"}
    return {"Direction": direction_name, "sub" : "Right"}
