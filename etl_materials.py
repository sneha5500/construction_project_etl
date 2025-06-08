import pandas as pd
import sqlite3

# Extract
df = pd.read_csv("materials.csv")

# Calculate remaining materials
df["remaining_qty"] = df["material_qty"] - df["used_qty"]

# Load
conn = sqlite3.connect("company.db")

# Update schema if not exists
conn.execute('''
CREATE TABLE IF NOT EXISTS Materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_id INTEGER,
    material_name TEXT,
    material_qty INTEGER,
    used_qty INTEGER,
    cost REAL,
    remaining_qty INTEGER
)
''')

# Clear old data (optional if you're resetting)
conn.execute("DELETE FROM Materials")

# Insert
df.to_sql("Materials", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("✅ Materials with remaining quantity loaded successfully!")


