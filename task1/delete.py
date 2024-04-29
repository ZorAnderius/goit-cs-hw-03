import psycopg2
import logging

from dotenv import dotenv_values
from psycopg2 import DatabaseError

from queries.delete_sql import delete_tasks_by_id
from find import find_sql, show_result
from queries.find_sql import find_task_by_id

config = dotenv_values("./task1/.env")

def delete_sql(conn, sql, id=""):
    try:
        cur = conn.cursor()
        cur.execute(sql, (id,))
    except DatabaseError as e:
        logging.error(f"Database error: {str(e)}")
        conn.rollback()
        raise DatabaseError("Issue with delete_sql")

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
            task_by_id = find_sql(conn, find_task_by_id, 3)
            show_result(task_by_id)

            print("Update task's status!\n")
            delete_sql(conn, delete_tasks_by_id, 3)

            print("Find task by id after update")
            task_by_id = find_sql(conn, find_task_by_id, 3)
            show_result(task_by_id)
        else:
            print("Error! Cannot create the database connection!")
    except DatabaseError as e:
        logging.error(f"Database error: {str(e)}")
        conn.rollback()
    finally:
        conn.close()
