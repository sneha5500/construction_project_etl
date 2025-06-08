import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv("work_hours.csv")

# Connect to DB
conn = sqlite3.connect("company.db")

# Insert into WorkHours table
df.to_sql("WorkHours", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("✅ WorkHours data loaded successfully!")

