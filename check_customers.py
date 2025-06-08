import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Customers")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

