import mysql.connector
from mysql.connector import Error
from config import config


def list_admin():
    with mysql.connector.connect(**config.MYSQL_DB_CONFIG) as conn:
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM fastapi_users")
            results = cur.fetchall()
        except Error as err:
            print("쿼리 에러: {err}")
            results = False
    return results


def create_admin(name: str):
    with mysql.connector.connect(**config.MYSQL_DB_CONFIG) as conn:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO fastapi_users (user_name) VALUES (%s)", (name,))
            conn.commit()
            result = cur.lastrowid
            print(result)
        except Error as err:
            print("쿼리 에러: " + str(err))
            result = False
    return result


def delete_admin(user_id: int):
    with mysql.connector.connect(**config.MYSQL_DB_CONFIG) as conn:
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM fastapi_users WHERE user_id = %s", (user_id,))
            conn.commit()
            result = cur.rowcount
        except Error as err:
            print("쿼리 에러: " + str(err))
            result = False
    return result
