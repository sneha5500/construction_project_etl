import pandas as pd

# Load the CSV
df = pd.read_csv("ownership_transfers.csv")

# Drop the transfer_id column if it exists
if 'transfer_id' in df.columns:
    df.drop(columns=['transfer_id'], inplace=True)

# Save back to the same CSV
df.to_csv("ownership_transfers.csv", index=False)

print("✅ transfer_id column removed successfully.")
