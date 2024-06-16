import sqlite3

def addApps(path: str):
    conn = sqlite3.connect("System/Config/appList.db")

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            app_name TEXT NOT NULL,
            app_path TEXT NOT NULL,
            app_version TEXT NOT NULL,
            app_default INTEGER DEFAULT 1 -- 1 for True, 0 for False
        )
    ''')

    conn.commit()

# def add_app():