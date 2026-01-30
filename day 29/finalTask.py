import pandas as pd

# 1. Create a DataFrame with Name, Age, Marks

data = {
    "Name": ["Bibek","Sumit","Arbin"],
    "Age": [21,17,20],
    "Marks": [45, 92, 57]
}

df = pd.DataFrame(data)

#2. Add Percentage column

df["Percentage"] = [31, 90, 59]

#3. Filter students with Percentage > 80
print(df["Percentage"] > 80)

# 4. Sort by Marks descending
df = df.sort_values(by="Marks", ascending=False)


# 5. Save result to CSV
df.to_csv("output.csv", index=False)


