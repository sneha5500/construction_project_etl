import pandas as pd
import sqlite3

# Extract
df = pd.read_csv("external_sites.csv")

# Transform
df.rename(columns={
    'plot_id': 'site_id',
    'location_name': 'location',
    'area_name': 'area_name',
    'size_in_sqft': 'area_sqft',
    'rate': 'cost_per_sqft'
}, inplace=True)

df['status'] = 'available'
df['current_owner_id'] = None

# Load
conn = sqlite3.connect("company.db")

# Create table if not exists (now includes area_name)
conn.execute('''
CREATE TABLE IF NOT EXISTS Sites (
    site_id INTEGER PRIMARY KEY,
    location TEXT,
    area_name TEXT,
    area_sqft INTEGER,
    cost_per_sqft INTEGER,
    status TEXT,
    current_owner_id INTEGER
)
''')

df.to_sql("Sites", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("✅ ETL completed. Data inserted into company.db")
