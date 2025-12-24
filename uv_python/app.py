from typing import Annotated
from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Annotated[str, Query(min_length=3)] = None):
    return {"item_id": item_id, "q":q}