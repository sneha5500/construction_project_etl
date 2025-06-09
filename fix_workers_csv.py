import pandas as pd

df = pd.read_csv("workers.csv")

# Drop worker_id if exists
if 'worker_id' in df.columns:
    df = df.drop(columns=['worker_id'])

df.to_csv("workers.csv", index=False)
print("✅ Cleaned workers.csv (removed worker_id)")
