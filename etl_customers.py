import pandas as pd
import sqlite3

# Load the CSV
df = pd.read_csv("customers.csv")

# Connect to DB
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    phone TEXT,
    email TEXT
)
''')

# Insert into DB
df.to_sql("Customers", conn, if_exists="append", index=False)

print("✅ Customers data loaded successfully!")

conn.commit()
conn.close()


