# pylint: disable=missing-docstring

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id : UUID
    title : str = Field(min_length=1)
    author : str = Field(min_length=1, max_length=100)
    description : Optional[str] = Field(title="Description of book", min_length=1, max_length=100)
    rating : int = Field(ge=0, le = 100)
    
    model_config = {
        "json_schema_extra" : {
            "example":{
                "id" : "1333e242-49d6-4700-a3da-817c1be34443",
                "title" : "Computer science pro",
                "author" : "Codify",
                "description" : "Nice description",
                "rating" : 75
            }
        }
    }

BOOKS = []

@app.get("/")
async def read_all_books():
    if len(BOOKS) < 1:
        create_book_no_api()
    return BOOKS

@app.post("/")
async def create_book(book : Book):
    BOOKS.append(book)
    return book

def create_book_no_api():
    book_1 = Book(id = "d333e242-49d6-4700-a3da-817c1be34443",
                  title ="title 1",
                  author = "author 1",
                  description = "description 1",
                  rating = 60)
    book_2 = Book(id = "d333e282-49d6-4700-a3da-817c1be34443",
                  title ="title 2",
                  author = "author 2",
                  description = "description 2",
                  rating = 70)
    book_3 = Book(id = "d333e232-49d6-4700-a3da-817c1be34443",
                  title ="title 3",
                  author = "author 3",
                  description = "description 3",
                  rating = 10)
    book_4 = Book(id = "E333e232-49d6-4700-a3da-817c1be34443",
                  title ="title 4",
                  author = "author 4",
                  description = "description 4",
                  rating = 100)
    
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)