from datetime import datetime
from sqlmodel import Field, SQLModel

class UserBase(SQLModel):
	email: str
	username: str
	last_login: datetime
	is_admin: bool

class User(UserBase, table=True):
	id: int = Field(default=None, primary_key=True)