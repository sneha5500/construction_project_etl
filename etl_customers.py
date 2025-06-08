import pandas as pd
import sqlite3

# Extract
df = pd.read_csv("customers.csv")

# Transform
df['email'] = df['email'].str.lower()

# Load
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    phone TEXT,
    email TEXT
)
''')

# Insert data (skip if ID already exists)
for _, row in df.iterrows():
    try:
        cursor.execute(
            "INSERT INTO Customers (customer_id, customer_name, phone, email) VALUES (?, ?, ?, ?)",
            (row['customer_id'], row['customer_name'], row['phone'], row['email'])
        )
    except sqlite3.IntegrityError:
        pass  # Skip duplicates

conn.commit()
conn.close()

