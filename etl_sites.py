import pandas as pd
import sqlite3
import random

# Step 1: Read your original data
df = pd.read_csv("sites.csv")

# Step 2: Add random realistic cost per sqft (₹1800 to ₹3000)
df["cost_per_sqft"] = [random.randint(1800, 3000) for _ in range(len(df))]

# Step 3: Add random status
df["status"] = [random.choice(["Under Construction", "Completed", "Planning"]) for _ in range(len(df))]

# Step 4: Add site_id (starting from 1)
df.insert(0, "site_id", range(1, len(df)+1))

# Step 5: Load into SQLite DB
conn = sqlite3.connect("company.db")
df.to_sql("Sites", conn, if_exists="replace", index=False)
conn.close()

print("✅ Sites table updated and loaded successfully.")




