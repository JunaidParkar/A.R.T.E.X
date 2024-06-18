import sqlite3

class AppRegistry():

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.registryTableName = "appRegistry"


    def __init__connection__(self):
        self.conn = sqlite3.connect("System/Config/appList.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.registryTableName} (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                package_name TEXT NOT NULL,
                version TEXT NOT NULL,
                is_default INTEGER DEFAULT 1 /* 1 for True, 0 for False */
            )
        """)
        self.conn.commit()

    def addApps(self, name: str, package_name: str, version: str, default: int):
        self.__init__connection__()
        self.cursor.execute(f"INSERT INTO {self.registryTableName} (name, package_name, version, is_default) VALUES ('{str(name)}', '{str(package_name)}', '{str(version)}', {default})")
        self.conn.commit()
        self.conn.close()
        return

    def remove_apps(self, package_name: str):
        self.__init__connection__()
        self.cursor.execute(f"DELETE FROM {self.registryTableName} WHERE package_name='{str(package_name)}'")
        self.conn.commit()
        self.conn.close()


    def update_apps(self, old_packagename: str, name: str, package_name: str, version: str, default: int):
        self.__init__connection__()
        self.cursor.execute(f"UPDATE {self.registryTableName} SET name='{str(name)}', package_name='{str(package_name)}', version='{str(version)}', is_default={default} WHERE package_name='{str(old_packagename)}'")
        self.conn.commit()
        self.conn.close()

    def get_allApps(self):
        self.__init__connection__()
        self.cursor.execute(f"SELECT * FROM {self.registryTableName}")
        data = self.cursor.fetchall()
        self.conn.close()
        return data
        
    def getApp(self, package_name: str):
        self.__init__connection__()
        self.cursor.execute(f"SELECT * FROM {self.registryTableName} WHERE package_name='{str(package_name)}'")
        data = self.cursor.fetchone()
        self.conn.close()
        return data
    

class EnvironmentVariables():

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.registryTableName = "environment"


    def __init__connection__(self):
        self.conn = sqlite3.connect("System/Config/environment.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.registryTableName} (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                path TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_environment(self, name: str, path: str):
        self.__init__connection__()
        self.cursor.execute(f"INSERT INTO {self.registryTableName} (name, path) VALUES ('{str(name)}', '{str(path)}')")
        self.conn.commit()
        self.conn.close()
        return

    def remove_environment(self, name: str):
        self.__init__connection__()
        self.cursor.execute(f"DELETE FROM {self.registryTableName} WHERE name='{str(name)}'")
        self.conn.commit()
        self.conn.close()


    def update_environment(self, old_name: str, name: str, path: str):
        self.__init__connection__()
        self.cursor.execute(f"UPDATE {self.registryTableName} SET name='{str(name)}', package_name='{str(path)}' WHERE name='{str(old_name)}'")
        self.conn.commit()
        self.conn.close()

    def get_all_environment(self):
        self.__init__connection__()
        self.cursor.execute(f"SELECT * FROM {self.registryTableName}")
        data = self.cursor.fetchall()
        self.conn.close()
        return data
        
    def get_environment(self, name: str):
        self.__init__connection__()
        self.cursor.execute(f"SELECT * FROM {self.registryTableName} WHERE name='{str(name)}'")
        data = self.cursor.fetchone()
        self.conn.close()
        return data