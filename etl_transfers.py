import pandas as pd
import sqlite3

# Extract
df = pd.read_csv("ownership_transfers.csv")

# Load
conn = sqlite3.connect("company.db")

# Create table if not exists
conn.execute('''
CREATE TABLE IF NOT EXISTS OwnershipTransfers (
    transfer_id INTEGER PRIMARY KEY,
    site_id INTEGER,
    customer_id INTEGER,
    transfer_date TEXT,
    price_paid INTEGER,
    FOREIGN KEY(site_id) REFERENCES Sites(site_id),
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
)
''')

# Insert transfer data
df.to_sql("OwnershipTransfers", conn, if_exists="append", index=False)

# Update current_owner_id in Sites table
for _, row in df.iterrows():
    conn.execute('''
    UPDATE Sites
    SET current_owner_id = ?
    WHERE site_id = ?
    ''', (row['customer_id'], row['site_id']))

conn.commit()
conn.close()

print("✅ Ownership transfers loaded and site ownership updated.")
