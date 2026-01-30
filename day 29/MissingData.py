import pandas as pd
import numpy as np

data = {
    "Name": ["Bibek", "Ram", "Sita", "Hari", np.nan, "Laxman", "Shyam", "Rita", "Suman", "Kiran"],
    "Subject": ["DSA", "Web Tech", "SAD", np.nan, "DBMS", "OS", "CN", "SE", np.nan, "AI"],
}

df = pd.DataFrame(data)

# print(df.isna()) #retruningn true false for missing data

print(df.isna().sum()) #counting missing data

df["Name"] = df["Name"].fillna("Unknown") #filling missing data with a specific value

df["Subject"] = df["Subject"].fillna("Harrypotter") #filling missing data with a specific value

df["Age"] = [25, 30, np.nan, 22, 24, 27, 30, 23, 26, 31]

df["Age"] = df["Age"].fillna(df["Age"].mean()) #filling missing data with mean value of the column
print(df)