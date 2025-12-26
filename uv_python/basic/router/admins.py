from typing import Annotated
from fastapi import APIRouter, Query
from model import mysql_study

router = APIRouter(
    prefix="/admins", tags=["admins"], responses={404: {"description": "Not Found"}}
)


@router.get("/list")
def read_admin():
    results = mysql_study.list_admin()
    return results


@router.post("/")
def create_admin(name: Annotated[str, Query(min_length=3)]):
    result = mysql_study.create_admin(name)
    return {"name": name, "id": result}


@router.delete("/{user_id}")
def delete_admin(user_id: int):
    result = mysql_study.delete_admin(user_id)
    return {"deleted_count": result}
