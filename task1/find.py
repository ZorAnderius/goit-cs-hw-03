import psycopg2
import logging

from dotenv import dotenv_values
from psycopg2 import DatabaseError

from queries.find_sql import (
    find_user_by_id,
    find_task_by_id,
    find_tasks_by_status,
    find_users_without_tasks,
    find_tasks_without_done,
    find_users_by_email,
    count_tasks_by_status,
    tasks_for_users_with_domain,
    find_tasks_without_desc,
    find_users_and_tasks_in_progress,
    find_users_task_count
)

config = dotenv_values("./task1/.env")

def find_sql(conn, sql, val=""):
    try:
        cur = conn.cursor()
        cur.execute(sql, (val,))
        rows = cur.fetchall()
        return rows
    except DatabaseError as e:
        logging.error(f"Database error: {str(e)}")
        conn.rollback()
        raise DatabaseError("Issue with find_sql")

def show_result(result):
    if not result:
        print("No result")
        return
    [print(row) for row in result]
    print("\n")

if __name__ == "__main__":
    try:
        conn = psycopg2.connect(
            host="localhost",
            database=config["NAME_DB"],
            user=config["USER_DB"],
            password=config["PASSWORD_DB"]
        )
        if conn is not None:
            print("Find user by id")
            user_by_id = find_sql(conn, find_user_by_id, 1)
            show_result(user_by_id)

            # print("Find task by id")
            # task_by_id = find_sql(conn, find_task_by_id, 3)
            # show_result(task_by_id)

            # print("Find tasks by status")
            # tasks_by_status = find_sql(conn, find_tasks_by_status, "new")
            # show_result(tasks_by_status)

            # print("Find users without tasks")
            # users_without_tasks = find_sql(conn, find_users_without_tasks)
            # show_result(users_without_tasks)

            # print("Find tasks without done")
            # tasks_without_done = find_sql(conn, find_tasks_without_done)
            # show_result(tasks_without_done)

            # print("Find users by email")
            # users_by_email = find_sql(conn, find_users_by_email, "%@example.org%")
            # show_result(users_by_email)

            # print("Count tasks by status")
            # count_tasks = find_sql(conn, count_tasks_by_status)
            # show_result(count_tasks)

            # print("Find tasks for users with domain")
            # users_with_domain = find_sql(conn, tasks_for_users_with_domain)
            # show_result(users_with_domain)

            # print("Find tasks without description")
            # tasks_without_des = find_sql(conn, find_tasks_without_desc)
            # show_result(tasks_without_des)

            # print("Find users and tasks in progress")
            # users_and_tasks_in_progress = find_sql(conn, find_users_and_tasks_in_progress)
            # show_result(users_and_tasks_in_progress)

            # print("Find users and task count")
            # users_task_count = find_sql(conn, find_users_task_count)
            # show_result(users_task_count)
        else:
            print("Error! Cannot create the database connection!")
    except DatabaseError as e:
            logging.error(e)
            conn.rollback()
    finally:
            conn.close()
