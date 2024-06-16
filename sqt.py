import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER
);
''')

# Insert data
cursor.execute('''
INSERT INTO users (name, email, age) VALUES (?, ?, ?);
''', ('Alice', 'alice@example.com', 30))

cursor.execute('''
INSERT INTO users (name, email, age) VALUES (?, ?, ?);
''', ('Bob', 'bob@example.com', 25))

# Select data
cursor.execute('''
SELECT * FROM users;
''')
print(cursor.fetchall())

# Update data
cursor.execute('''
UPDATE users SET age = ? WHERE name = ?;
''', (35, 'Alice'))

# Delete data
cursor.execute('''
DELETE FROM users WHERE name = ?;
''', ('Bob',))

# Select data to verify changes
cursor.execute('''
SELECT * FROM users;
''')
print(cursor.fetchall())

# Drop table
cursor.execute('''
DROP TABLE IF EXISTS users;
''')

# Commit the changes and close the connection
connection.commit()
connection.close()
