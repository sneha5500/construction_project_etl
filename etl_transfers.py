import pandas as pd
import sqlite3

# Connect to DB
conn = sqlite3.connect("company.db")

# Read CSV
df = pd.read_csv("ownership_transfers.csv")

# Load into DB
df.to_sql("OwnershipTransfers", conn, if_exists="append", index=False)

conn.close()

print("✅ OwnershipTransfers data loaded successfully.")

