from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/items", tags=["items"], responses={404: {"description": "Not Found"}}
)


@router.get("/{item_id}")
def read_item(item_id: int, q: Annotated[str, Query(min_length=3)] = None):
    return {"item_id": item_id, "q": q}
