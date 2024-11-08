import sqlite3

class AppRegistry:
    def __init__(self, db_name=r'C:\Users\verix\Documents\xampp\htdocs\A.R.T.E.X\System\Config\registry.db'):
        self.__db_name = db_name
        self.__create_table()

    def __create_table(self):
        with sqlite3.connect(self.__db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS apps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    app_name TEXT NOT NULL,
                    app_package_name TEXT NOT NULL,
                    version TEXT NOT NULL,
                    is_default_app INTEGER NOT NULL
                )
            ''')
            conn.commit()

    def register_app(self, app_name, app_package_name, version, is_default_app):
        with sqlite3.connect(self.__db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO apps (app_name, app_package_name, version, is_default_app)
                VALUES (?, ?, ?, ?)
            ''', (app_name, app_package_name, version, is_default_app))
            conn.commit()
            conn.close()

    def get_app(self, app_package_name):
        with sqlite3.connect(self.__db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM apps WHERE app_package_name = ?', (app_package_name,))
            app = cursor.fetchone()
            conn.close()
            return app

    def read_apps(self):
        with sqlite3.connect(self.__db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM apps')
            apps = cursor.fetchall()
            conn.close()
            return apps

    def update_app(self, app_id, app_name=None, app_package_name=None, version=None, is_default_app=None):
        with sqlite3.connect(self.__db_name) as conn:
            cursor = conn.cursor()
            if app_name is not None:
                cursor.execute('''
                    UPDATE apps
                    SET app_name = ?
                    WHERE id = ?
                ''', (app_name, app_id))
            if app_package_name is not None:
                cursor.execute('''
                    UPDATE apps
                    SET app_package_name = ?
                    WHERE id = ?
                ''', (app_package_name, app_id))
            if version is not None:
                cursor.execute('''
                    UPDATE apps
                    SET version = ?
                    WHERE id = ?
                ''', (version, app_id))
            if is_default_app is not None:
                cursor.execute('''
                    UPDATE apps
                    SET is_default_app = ?
                    WHERE id = ?
                ''', (is_default_app, app_id))
            conn.commit()
            conn.close()

    def delete_app(self, packageName):
        with sqlite3.connect(self.__db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM apps WHERE app_package_name = ?', (packageName,))
            conn.commit()
            conn.close()