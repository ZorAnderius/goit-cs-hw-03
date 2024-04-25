sql_insert_user = "INSERT INTO users (fullname, email) VALUES (%s, %s)"

sql_insert_status = "INSERT INTO status (name) VALUES (%s)"

sql_insert_tasks = (
    "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)"
)

# Додати нове завдання для конкретного користувача.
# Використайте INSERT для додавання нового завдання.
insert_new_task_for_user = """
        INSERT INTO tasks (title, description, user_id, status_id)
        VALUES ('New Task Title', 'New Task Description', %s, %s);
        """
