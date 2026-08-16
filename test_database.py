import sqlite3

conn = sqlite3.connect("crop.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM crops")

data = cursor.fetchall()

print(data)

conn.close()