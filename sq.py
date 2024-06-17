import sqlite3

class appRegistry():

    def __init__(self):
        pass

    def addApps(self, name: str, package_name: str, version: str, default: int):
        conn = sqlite3.connect("System/Config/appList.db")

        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS appRegistry (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                package_name TEXT NOT NULL,
                version TEXT NOT NULL,
                is_default INTEGER DEFAULT 1 -- 1 for True, 0 for False
            )
        ''')

        conn.commit()

        cursor.execute(f"INSERT INTO appRegistry (name, package_name, version, is_default) VALUES ('{str(name)}', '{str(package_name)}', '{str(version)}', {default})")

        conn.commit()
        conn.close()
        return

    def remove_apps(self, package_name: str):
        conn = sqlite3.connect("System/Config/aaa.db")

        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS aaa (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                package_name TEXT NOT NULL,
                version TEXT NOT NULL,
                is_default INTEGER DEFAULT 1 -- 1 for True, 0 for False
            )
        ''')

        conn.commit()

        cursor.execute(f"DELETE FROM aaa WHERE package_name='{str(package_name)}'")
        conn.commit()
        conn.close()


    def update_apps(self, old_packagename: str, name: str, package_name: str, version: str, default: int):
        conn = sqlite3.connect("System/Config/aaa.db")

        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS aaa (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                package_name TEXT NOT NULL,
                version TEXT NOT NULL,
                is_default INTEGER DEFAULT 1 -- 1 for True, 0 for False
            )
        ''')

        conn.commit()

        cursor.execute(f"UPDATE aaa SET name='{str(name)}', package_name='{str(package_name)}', version='{str(version)}', is_default={default} WHERE package_name='{str(old_packagename)}'")

        conn.commit()
        conn.close()

        def get_allApps(self):
            conn = sqlite3.connect("System/Config/appList.db")

            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS appRegistry (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    package_name TEXT NOT NULL,
                    version TEXT NOT NULL,
                    is_default INTEGER DEFAULT 1 -- 1 for True, 0 for False
                )
            ''')

            conn.commit()

            cursor.execute("SELECT * FROM aaa")

            data = cursor.fetchall()
        
        def getApp(self, package_name: str):
            conn = sqlite3.connect("System/Config/appList.db")

            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS appRegistry (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    package_name TEXT NOT NULL,
                    version TEXT NOT NULL,
                    is_default INTEGER DEFAULT 1 -- 1 for True, 0 for False
                )
            ''')

            conn.commit()

            cursor.execute(f"SELECT * FROM aaa WHERE package_name='{str(package_name)}'")
            return cursor.fetchone()

# update_apps("art.try9", "try", "art.try", "1.2.0", 1)

# remove_apps("art.try")


# addApps("Artex AI", "artex.chat", "1.0.0", 1)
# addApps("Terminal", "artex.cmd", "1.0.0", 1)
# addApps("File Manager", "artex.fileSystem", "1.0.0", 1)
# addApps("Setting", "artex.setting", "1.0.0", 1)
# addApps("Artex store", "artex.store", "1.0.0", 1)
# addApps("Artex", "artex.ui", "1.0.0", 1)

# addApps("try", "art.try", "1.0.0", 0)
# addApps("try1", "art.try1", "1.0.0", 0)
# addApps("try2", "art.try2", "1.0.0", 0)
# addApps("try3", "art.try3", "1.0.0", 0)
# addApps("try4", "art.try4", "1.0.0", 0)
# addApps("try5", "art.try5", "1.0.0", 0)