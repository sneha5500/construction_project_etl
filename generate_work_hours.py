import pandas as pd
import random

data = []
months = ["Feb", "Mar", "Apr", "May"]

# Simulate realistic work data for 3000 workers
for worker_id in range(1, 3001):
    for month in months:
        days_worked = random.randint(20, 26)
        hours_worked = days_worked * random.randint(6, 9)
        data.append([worker_id, month, days_worked, hours_worked])

df = pd.DataFrame(data, columns=["worker_id", "month", "total_days_worked", "total_hours_worked"])
df.to_csv("work_hours.csv", index=False)

print("✅ work_hours.csv generated!")

