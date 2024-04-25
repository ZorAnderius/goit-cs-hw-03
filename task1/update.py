import psycopg2
from dotenv import dotenv_values
from sqlite3 import Error

from queries.update_sql import update_tasks_status, update_username
from find import find_sql, show_result
from queries.find_sql import find_task_by_id, find_user_by_id

config = dotenv_values("./task1/.env")

conn = psycopg2.connect(
    host="localhost",
    database=config["NAME_DB"],
    user=config["USER_DB"],
    password=config["PASSWORD_DB"]
)


def update_sql(conn, sql, id="", value=""):
    try:
        cur = conn.cursor()
        cur.execute(sql, (value,id))
    except Error as e:
        print(e)

if __name__ == "__main__":
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
    conn.close()
