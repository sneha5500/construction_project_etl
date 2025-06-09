import pandas as pd

# Load the original CSV
df = pd.read_csv("customers.csv")

# Drop the customer_id column if it exists
if 'customer_id' in df.columns:
    df = df.drop(columns=['customer_id'])

# Save cleaned CSV back
df.to_csv("customers.csv", index=False)

print("✅ Cleaned customers.csv (removed customer_id)")
