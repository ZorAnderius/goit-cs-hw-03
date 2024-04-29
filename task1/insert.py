import psycopg2
import logging

from dotenv import dotenv_values
from psycopg2 import DatabaseError

from queries.insert_sql import insert_new_task_for_user
from find import find_sql, show_result
from queries.find_sql import find_user_by_id

config = dotenv_values("./task1/.env")

def insert_sql(conn, sql, user_id="", status_id=""):
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id, status_id))
        conn.commit()
    except DatabaseError as e:
        logging.error(f"Database error: {str(e)}")
        conn.rollback()
        raise DatabaseError("Issue with insert_sql" )


if __name__ == "__main__":
    try:
        conn = psycopg2.connect(
            host="localhost",
            database=config["NAME_DB"],
            user=config["USER_DB"],
            password=config["PASSWORD_DB"],
        )
        if conn is not None:
            print("Find task by id before update")
            user_by_id = find_sql(conn, find_user_by_id, 3)
            show_result(user_by_id)

            print("Insert task for user!\n")
            tasks_status = insert_sql(conn, insert_new_task_for_user, 3, 2)

            print("Find task by id after update")
            user_by_id = find_sql(conn, find_user_by_id, 3)
            show_result(user_by_id)
        else:
            print("Error! Cannot create the database connection!")
    except DatabaseError as e:
        logging.error(f"Database error: {str(e)}")
        conn.rollback()
    finally:
        conn.close()
