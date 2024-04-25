import psycopg2
from sqlite3 import Error
from dotenv import dotenv_values

from queries.create_sql import sql_create_user_table, sql_create_status_table, sql_create_tasks_table

config = dotenv_values("./task1/.env")


conn = psycopg2.connect(
    host="localhost",
    database=config["NAME_DB"],
    user=config["USER_DB"],
    password=config["PASSWORD_DB"]
)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

if __name__ == '__main__':
    if conn is not None:
        create_table(conn, sql_create_user_table)
        create_table(conn, sql_create_status_table)
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! Cannot create the database connection!")

    conn.close()
