import pandas as pd
import sqlite3

df = pd.read_csv("materials.csv")

conn = sqlite3.connect("company.db")

df.to_sql("Materials", conn, if_exists="append", index=False)

conn.close()
print("✅ Materials data loaded successfully.")



