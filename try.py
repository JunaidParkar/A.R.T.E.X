import requests
import sqlite3

class reminderDB:

    def __init__(self, db_name=r'C:\Users\verix\Documents\xampp\htdocs\A.R.T.E.X\System\Config\registry.db'):
        self.__db_name = db_name
        self.__create_table()

    def __create_table(self):
        with sqlite3.connect(self.__db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reminder (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    completed INTEGER NOT NULL
                )
            ''')
            conn.commit()

    def addReminder(self, inp):
        with sqlite3.connect(self.__db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO reminder (task, date, time, completed)
                VALUES (?, ?, ?, ?)
            ''', (inp["task"], inp["date"], inp["time"], 0))
            conn.commit()

class reminderHouse:

    def __init__(self):
        self.__dbManager = reminderDB()
        pass

    def setReminder(self, prompt):
        try:
            response = requests.post("http://localhost:3000/task", json={"prompt": prompt})
            response.raise_for_status()  # Raise an error for bad status codes
            resp_json = response.json()

            # Validate response format
            if "response" in resp_json and all(k in resp_json["response"] for k in ["task", "date", "time"]):
                resp = resp_json["response"]
                self.__dbManager.addReminder(resp)
            else:
                print("Invalid response format:", resp_json)

        except requests.exceptions.RequestException as e:
            print(f"Error with the HTTP request: {e}")
        except KeyError as e:
            print(f"KeyError: {e}")



a = reminderHouse()
a.setReminder("remind me for dinner at 6 evening")