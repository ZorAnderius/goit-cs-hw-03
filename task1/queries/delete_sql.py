# Видалити конкретне завдання.
# Використайте DELETE для видалення завдання за його id.
delete_tasks_by_id = """
                DELETE FROM tasks 
                WHERE id = %s
                """
