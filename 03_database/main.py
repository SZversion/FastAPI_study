from fastapi import Depends, FastAPI
from sqlmodel import select
from database.connection import conn, get_session
from models.users import User

app = FastAPI()

@app.on_event("startup")
def on_startup():
	conn()

@app.get("/")
async def get_user(session=Depends(get_session)):
	return session.exec(select(User)).all()


if __name__ == "__main__":
	import uvicorn
	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)