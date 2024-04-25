# Отримати всі завдання певного користувача.
# Використайте SELECT для отримання завдань конкретного користувача за його user_id.
find_user_by_id = """
                SELECT u.id, u.fullname, t.title, t.description, s."name" as status  
                FROM users u 
                LEFT JOIN tasks t ON u.id = t.user_id
                LEFT join status s ON t.status_id = s.id 
                WHERE u.id = %s
                ORDER BY u.fullname 
                """

# Вибрати завдання за певним статусом.
# Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
find_tasks_by_status = """
                SELECT t.title, t.description, s."name" as status  
                FROM status s 
                LEFT JOIN tasks t ON s.id = t.status_id
                WHERE s."name" = %s
                ORDER BY t.title
                """

# Отримати список користувачів, які не мають жодного завдання.
# Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
find_users_without_tasks = """
                SELECT u.id, u.fullname, u.email 
                FROM users u 
                WHERE u.id NOT IN (
                    SELECT t.user_id 
                    FROM tasks t
                    )
                """

# Отримати всі завдання, які ще не завершено.
# Виберіть завдання, чий статус не є 'завершено'.
find_tasks_without_done = """
                SELECT t.title, t.description, s."name" as status  
                FROM status s 
                lEFT JOIN tasks t ON s.id = t.status_id
                WHERE s."name" != 'done'
                ORDER BY t.title
                """

# Знайти користувачів з певною електронною поштою.
# Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
find_users_by_email = """
                SELECT u.id, u.fullname, u.email 
                FROM users u 
                WHERE u.email LIKE %s
                """

# Отримати кількість завдань для кожного статусу.
# Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
count_tasks_by_status = """
                SELECT s."name" as status, COUNT(t.id) as count 
                FROM status s 
                LEFT JOIN tasks t ON s.id = t.status_id
                GROUP BY s."name"
                """

# Отримати завдання, які призначені користувачам з певною доменною частиною
# електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN,
# щоб вибрати завдання, призначені користувачам, чия електронна пошта містить
# певний домен (наприклад, '%@example.com').
tasks_for_users_with_domain = """
                SELECT t.id, t.description 
                FROM tasks t 
                JOIN users u ON t.user_id = u.id  
                WHERE u.email LIKE %s
                """

# Отримати список завдань, що не мають опису.
# Виберіть завдання, у яких відсутній опис.
find_tasks_without_desc = """
                SELECT t.id, t.title 
                FROM tasks t 
                WHERE t.description IS NULL;
                """

# Вибрати користувачів та їхні завдання, які є
# у статусі 'in progress'. Використайте INNER JOIN
# для отримання списку користувачів та їхніх завдань
# із певним статусом.
find_users_and_tasks_in_progress = """
                SELECT u.id, u.fullname, t.title, t.description, s."name" as status  
                FROM users u 
                LEFT JOIN tasks t ON u.id = t.user_id
                LEFT JOIN status s ON t.status_id = s.id 
                WHERE s."name" = 'in progress'
                ORDER BY u.id
                """

# Отримати користувачів та кількість їхніх завдань.
# Використайте LEFT JOIN та GROUP BY для вибору користувачів
# та підрахунку їхніх завдань.
find_users_task_count = """
                SELECT u.id, u.fullname, COUNT(t.id) AS task_count
                FROM users u 
                LEFT JOIN tasks t ON u.id = t.user_id
                GROUP BY u.id, u.fullname;
                """

find_task_by_id = """
                SELECT t.id, t.title, t.description, s."name" as status  
                FROM status s 
                LEFT JOIN tasks t ON s.id = t.status_id
                WHERE t.id = %s
                ORDER BY t.title
                """
