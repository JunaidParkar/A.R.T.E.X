import requests
import sqlite3
import datetime

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

    def __check_time_under_zone(self, t, timeout=5):
        current_time = datetime.datetime.now()
        # Convert the input time string to a datetime object
        given_time = datetime.datetime.strptime(t, '%H:%M')
        # Replace the date of the given time with the current date to ensure comparison is only for time
        given_time = current_time.replace(hour=given_time.hour, minute=given_time.minute, second=0, microsecond=0)
        # Calculate the time difference
        time_difference = abs(current_time - given_time)

        return time_difference <= datetime.timedelta(minutes=timeout)

    def addReminder(self, inp):
        with sqlite3.connect(self.__db_name) as conn:
            cursor = conn.cursor()

            if inp["time"] == "unspecified":
                conn.close()
                return "Time is not specified"
            
            if inp["date"] == "unspecified":
                if datetime.datetime.now().strftime('%H:%M') > inp["time"]:
                    new_date = datetime.datetime.today() + datetime.timedelta(days=1)
                    inp["date"] = new_date.strftime('%Y-%m-%d')
                else:
                    inp["date"] = datetime.datetime.today().strftime('%Y-%m-%d')
            
            if inp["task"] == "unspecified":
                conn.close()
                return "Task is not specified"
            
            if datetime.datetime.today().strftime('%Y-%m-%d') > inp["date"]:
                conn.close()
                return "The date mentioned is already past."

            if datetime.datetime.today().strftime('%Y-%m-%d') == inp["date"] or inp["date"].lower() == "today":
                print("by first")
                if inp["date"] == "today":
                    inp["date"] = datetime.datetime.today().strftime('%Y-%m-%d')
                if datetime.datetime.now().strftime('%H:%M') < inp["time"]:
                    tz = self.__check_time_under_zone(5)
                    if not tz:
                        conn.close()
                        return "The time for reminder is less than that of 5 minutes. I guess you must remember it by yourself sir to practise your brain memory."
                
                    inp["date"] = datetime.datetime.today().strftime('%Y-%m-%d') if inp["date"] == "today" else (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d') if inp["date"] == "tomorrow" else inp["date"]
                
                    cursor.execute('''
                        INSERT INTO reminder (task, date, time, completed)
                        VALUES (?, ?, ?, ?)
                    ''', (inp["task"], inp["date"], inp["time"], 0))
                    conn.commit()
                    conn.close()
                    return "Reminder added succesfully"
                
                else: 
                    conn.close()
                    return "Time is incorrect or have already passed"
            elif datetime.datetime.today().strftime('%Y-%m-%d') < inp["date"] or inp["date"].lower()  == "tomorrow":
                print("by sec")
                # return "Either the date is already passed or its incorrect"
                inp["date"] = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d') if inp["date"] == "tomorrow" else inp["date"]
                cursor.execute('''
                        INSERT INTO reminder (task, date, time, completed)
                        VALUES (?, ?, ?, ?)
                    ''', (inp["task"], inp["date"], inp["time"], 0))
                conn.commit()
                conn.close()
                return "Reminder added succesfully"
            else:
                conn.close()
                return "Date passed"

            
    def get_non_alerted_passed_reminders(self):
        with sqlite3.connect(self.__db_name) as conn:
            cursor = conn.cursor()
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            current_time = datetime.datetime.now().strftime('%H:%M')
            # Query to select rows where completed is 0 and both date and time have passed
            cursor.execute('''
                SELECT * FROM reminder
                WHERE completed = 0
                AND (date < ? OR date = ?)
                AND (time < ?)
            ''', (current_date, current_date, current_time))
            
            rows = cursor.fetchall()  # Fetch all rows matching the criteria
        return rows

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
                return self.__dbManager.addReminder(resp)
            else:
                print("Invalid response format:", resp_json)

        except requests.exceptions.RequestException as e:
            print(f"Error with the HTTP request: {e}")
        except KeyError as e:
            print(f"KeyError: {e}")

    def get_un_notified_reminder(self):
        return self.__dbManager.get_non_alerted_passed_reminders()

a = reminderHouse()
# b = a.setReminder("remind me for dinner at 12 morning on 20 August")
b = a.get_un_notified_reminder()
print(b)