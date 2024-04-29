import psycopg2
import logging

from dotenv import dotenv_values
from psycopg2 import DatabaseError

from queries.update_sql import update_tasks_status, update_username
from find import find_sql, show_result
from queries.find_sql import find_task_by_id, find_user_by_id

config = dotenv_values("./task1/.env")

def update_sql(conn, sql, id="", value=""):
    try:
        cur = conn.cursor()
        cur.execute(sql, (value,id))
    except DatabaseError as e:
        logging.error(f"Database error: {str(e)}")
        conn.rollback()
        raise DatabaseError("Issue with update_sql")

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
            tasks_status = update_sql(conn, update_tasks_status, 3, 'done')

            print("Find task by id after update")
            task_by_id = find_sql(conn, find_task_by_id, 3)
            show_result(task_by_id)

            # print("Find user by id before update")
            # user_by_id = find_sql(conn, find_user_by_id, 1)
            # show_result(user_by_id)

            # print("Update user's names!\n")
            # user_name = update_sql(conn, update_username, 1, "John Show")

            # print("Find user by id after update")
            # user_by_id = find_sql(conn, find_user_by_id, 1)
            # show_result(user_by_id)
        else:
            print("Error! Cannot create the database connection!")
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        conn.close()
