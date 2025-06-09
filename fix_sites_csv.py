import pandas as pd

df = pd.read_csv("sites.csv")

# Drop site_id if exists
if 'site_id' in df.columns:
    df = df.drop(columns=['site_id'])

df.to_csv("sites.csv", index=False)
print("✅ Cleaned sites.csv (removed site_id)")

