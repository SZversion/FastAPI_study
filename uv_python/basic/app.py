from typing import Optional
from fastapi import FastAPI, HTTPException
from router import items, users, admins
from pydantic import BaseModel, Field
from enum import Enum
import nanoid

app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)
app.include_router(admins.router)

type ItemId = str


@app.get("/")
def read_root():
    return {"Hello": "World!"}


class ItemColor(str, Enum):
    red = "red"
    green = "green"
    blue = "blue"


class PersonBase(BaseModel):
    name: str = Field(description="이름")
    color: Optional[ItemColor] = Field(default=None, description="좋아하는 색상")


class Person(PersonBase):
    id: ItemId = Field(description="사람 ID")


temp_persons = {
    1: Person(id="asdfwer152", name="사람1", color=ItemColor.red),
    2: Person(id="1qwerasdf2", name="사람2", color=ItemColor.blue),
}


@app.get("/persons/{person_id}")
def read_person(person_id: ItemId) -> Person:
    # -> Person:  반환 타입 힌트
    for person in temp_persons.values():
        if person.id == person_id:
            return person
    else:
        raise HTTPException(status_code=404, detail="없는 사람")


@app.post("/persons", summary="사람 생성", status_code=201)
def create_person(person: PersonBase) -> Person:
    person_id = nanoid.generate(size=10)

    if person_id in temp_persons:
        raise HTTPException(status_code=404, detail="이미 있는 사람")
    # temp_persons[person_id] = Person(id=person_id, name=person.name, color=person.color)
    temp_persons[person_id] = Person(id=person_id, **person.model_dump())
    return temp_persons[person_id]


@app.put("/persons/{person_id}", summary="사람 수정")
def update_person(person_id: ItemId, person: PersonBase) -> Person:
    for key, temp_person in temp_persons.items():
        if temp_person.id == person_id:
            updated_person = Person(id=person_id, **person.model_dump())
            temp_persons[key] = updated_person
            return updated_person
    else:
        raise HTTPException(status_code=404, detail="없는 사람")
