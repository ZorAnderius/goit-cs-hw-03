# Оновити статус конкретного завдання.
# Змініть статус конкретного завдання на 'in progress' або інший статус.
update_tasks_status = """
                UPDATE tasks 
                SET status_id = (SELECT id FROM status WHERE "name" = %s) 
                WHERE id = %s;
                """


# Оновити ім'я користувача.
# Змініть ім'я користувача за допомогою UPDATE.
update_username = """
                UPDATE users 
                SET fullname = %s 
                WHERE id = %s;
                """
