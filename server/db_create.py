import sqlite3

conn = sqlite3.connect('database.db')
conn.execute(
    'CREATE TABLE todos (title TEXT NOT NULL, dueDate timestamp, isDone BIT)')
conn.close()
