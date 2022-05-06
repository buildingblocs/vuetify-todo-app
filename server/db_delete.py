import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('DROP TABLE todos')
conn.close()
