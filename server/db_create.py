import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE todos (title TEXT NOT NULL, isDone BIT)')
conn.close()
