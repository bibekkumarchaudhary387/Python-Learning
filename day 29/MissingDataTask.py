import numpy as np
import pandas as pd

data = {
    "Name": ["Bibek", "Ram", "Sita", "Hari", "Gita", "Laxman", "Shyam", "Rita", "Suman", "Kiran"],
    "Subject": ["DSA", "Web Tech", "SAD", "English", "DBMS", "OS", "CN", "SE", "ML", "AI"],
    "Marks": [90, 85, np.nan, 88, 92, 80, np.nan, 95, 89, 84]
}

df= pd.DataFrame(data)

print(df) #before handling missing data

#Replace missing marks with average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print(df) #after handling missing data