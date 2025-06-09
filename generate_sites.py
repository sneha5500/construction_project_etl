import pandas as pd
import random

cities = {
    "Hyderabad": ["Madhapur", "Kukatpally", "Banjara Hills", "Gachibowli", "Begumpet"],
    "Karimnagar": ["Ramnagar", "Vavilalapally", "Mankammathota", "Jyothinagar", "Subhashnagar"],
    "Bangalore": ["Indiranagar", "Whitefield", "Jayanagar", "Koramangala", "BTM Layout"]
}

data = []

for i in range(1, 3001):
    city = random.choice(list(cities.keys()))
    area = random.choice(cities[city])
    size = random.randint(800, 5000)  # realistic range for sqft

    data.append({
        "site_id": i,
        "location": city,
        "area_name": area,
        "site_size_sqft": size
    })

df = pd.DataFrame(data)
df.to_csv("sites.csv", index=False)
print("✅ 3000 site entries saved to sites.csv")
