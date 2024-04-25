sql_create_user_table = """
                                CREATE TABLE IF NOT EXISTS users(
                                    id SERIAL PRIMARY KEY,
                                    fullname VARCHAR(100),
                                    email VARCHAR(100) UNIQUE
                                );
                                """
sql_create_status_table = """
                                CREATE TABLE IF NOT EXISTS status(
                                    id SERIAL PRIMARY KEY,
                                    name VARCHAR(50) UNIQUE CHECK(name IN ('new', 'in progress', 'done'))
                            );
                                """
sql_create_tasks_table = """
                                CREATE TABLE IF NOT EXISTS tasks(
                                    id SERIAL PRIMARY KEY,
                                    title VARCHAR(100),
                                    description TEXT,
                                    status_id INTEGER,
                                    user_id INTEGER,
                                    FOREIGN KEY (status_id) REFERENCES status(id),
                                    FOREIGN KEY (user_id) REFERENCES users(id)
                                    ON DELETE CASCADE
                                );
                                """