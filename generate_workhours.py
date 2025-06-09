import pandas as pd
import random
from datetime import datetime, timedelta

# Load worker data
df_workers = pd.read_csv("workers.csv")

# Define the months and simulate 3–4 months of data
months = ["Feb", "Mar", "Apr", "May"]

records = []

for _, row in df_workers.iterrows():
    for month in months:
        days_worked = random.randint(20, 28)
        hours_per_day = random.randint(6, 10)
        total_hours = days_worked * hours_per_day
        records.append({
            "worker_id": row.name + 1,
            "month": month,
            "total_days_worked": days_worked,
            "total_hours_worked": total_hours
        })

df_hours = pd.DataFrame(records)
df_hours.to_csv("work_hours.csv", index=False)

print("✅ work_hours.csv generated with realistic data.")
