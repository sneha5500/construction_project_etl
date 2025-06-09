import pandas as pd
import sqlite3

df = pd.read_csv("workers.csv")

conn = sqlite3.connect("company.db")

df.to_sql("Workers", conn, if_exists="append", index=False)

conn.close()
print("✅ Workers data loaded successfully.")



