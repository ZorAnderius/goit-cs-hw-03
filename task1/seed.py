from faker import Faker
import psycopg2
from random import randint
from sqlite3 import Error
from dotenv import dotenv_values

from queries.insert_sql import sql_insert_user, sql_insert_status, sql_insert_tasks

config = dotenv_values("./task1/.env")


conn = psycopg2.connect(
    host="localhost",
    database=config["NAME_DB"],
    user=config["USER_DB"],
    password=config["PASSWORD_DB"],
)

def seed(conn, sql_query, values):
    try:
        cur = conn.cursor()
        cur.execute(sql_query, values)
        conn.commit()
    except Error as e:
        print(e)

def seed_users(conn, sql):
    fake = Faker()
    for _ in range(30):
        seed(conn, sql, (fake.name(), fake.email()))

def seed_tasks(conn, sql):
    fake = Faker()
    for _ in range(20):
        seed(conn, sql, (fake.word(), fake.text(), randint(1, 3), randint(1, 30)))

def seed_status(conn, sql):
    seed(conn, sql, ("new",))
    seed(conn, sql, ("in progress",))
    seed(conn, sql, ("done",))

if __name__ == "__main__":
    if conn is not None:
        seed_users(conn, sql_insert_user)
        seed_status(conn, sql_insert_status)
        seed_tasks(conn, sql_insert_tasks)
    else:
        print("Error! Cannot create the database connection!")

    conn.close()
