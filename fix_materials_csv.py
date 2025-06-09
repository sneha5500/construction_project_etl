import pandas as pd

df = pd.read_csv("materials.csv")

# Drop material_id if exists
if 'material_id' in df.columns:
    df = df.drop(columns=['material_id'])

df.to_csv("materials.csv", index=False)
print("✅ Cleaned materials.csv (removed material_id)")
