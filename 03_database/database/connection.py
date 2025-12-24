from sqlmodel import SQLModel, create_engine


database_file = 'sqlite3.db'

sqlite_url = f"sqlite:///{database_file}"

engine = create_engine(sqlite_url, echo=True)


def conn():
	# DB에 연결하여 선언된 테이블들이 존재하는지 확인하고
    # 없다면 테이블들을 생성해준다.
	SQLModel.metadata.create_all(engine)