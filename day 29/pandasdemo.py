import pandas as pd

# 1. Create a Dictionary of data
data = {
    "Name": ["Bibek", "Ram", "Sita"],
    "Age": [25, 30, 28],
    "City": ["Kathmandu", "Pokhara", "Lalitpur"]
}

# 2. Convert to DataFrame
df = pd.DataFrame(data)

print(df)