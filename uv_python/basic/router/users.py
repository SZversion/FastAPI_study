from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not Found"}}
)


@router.get("/{user_id}")
def read_item(user_id: int):
    return {"user_id": user_id}
