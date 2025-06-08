import pandas as pd
import sqlite3

# Extract
df = pd.read_csv("workers.csv")

# Transform (optional cleanup)
df['job_role'] = df['job_role'].str.title()


# Load
conn = sqlite3.connect("company.db")
import pandas as pd
import sqlite3

# Load data
df = pd.read_csv("workers.csv")

# Connect to DB
conn = sqlite3.connect("company.db")

# Create correct table
conn.execute('''
CREATE TABLE IF NOT EXISTS Workers (
    worker_id INTEGER PRIMARY KEY,
    worker_name TEXT,
    job_role TEXT,
    salary_per_day REAL
)
''')

# Load data into table
df.to_sql("Workers", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("✅ Workers table loaded successfully!")

