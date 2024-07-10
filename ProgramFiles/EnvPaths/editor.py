import sqlite3

class EnvironmentDatabase:
    def __init__(self):
        self.db_name = r"C:\Users\verix\Documents\xampp\htdocs\A.R.T.E.X\System\Config\variables.db"
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS environment (
            id INTEGER PRIMARY KEY,
            variable_name TEXT NOT NULL,
            file_path TEXT NOT NULL
        );
        """
        self.cursor.execute(create_table_sql)
        self.connection.commit()

    def create_variable(self, variable_name, file_path):
        insert_sql = "INSERT INTO environment (variable_name, file_path) VALUES (?, ?)"
        self.cursor.execute(insert_sql, (variable_name, file_path))
        self.connection.commit()

    def read_variables(self):
        select_sql = "SELECT * FROM environment"
        self.cursor.execute(select_sql)
        return self.cursor.fetchall()

    def update_variable(self, variable_id, variable_name, file_path):
        update_sql = "UPDATE environment SET variable_name = ?, file_path = ? WHERE id = ?"
        self.cursor.execute(update_sql, (variable_name, file_path, variable_id))
        self.connection.commit()

    def delete_variable(self, variable_id):
        delete_sql = "DELETE FROM environment WHERE id = ?"
        self.cursor.execute(delete_sql, (variable_id,))
        self.connection.commit()

    def get_variable_path(self, variable_name):
        select_sql = "SELECT file_path FROM environment WHERE variable_name = ?"
        self.cursor.execute(select_sql, (variable_name,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close_connection(self):
        self.connection.close()