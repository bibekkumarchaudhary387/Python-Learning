import numpy as np
import pandas as pd

data = {
    "Name": ["Bibek", "Ram", "Sita", "Hari", "Gita", "Laxman", "Shyam", "Rita", "Suman", "Kiran"],
    "Subject": ["DSA", "Web Tech", "SAD", "English", "DBMS", "OS", "CN", "SE", "ML", "AI"],
    "Marks": [90, 85, np.nan, 88, 92, 80, np.nan, 95, 89, 84]
}

df= pd.DataFrame(data)

df["Marks"] = df.sort_values(by="Marks", ascending=False, na_position="first")["Marks"].values #sorting the dataframe by Marks and updating the Marks column accordingly

df["Age"] = [25, 30, 31, 22, 24, 27, 30, 23, 26, 31]

# df["Age"] = df.sort_values(by=["Age", "Name"])["Age"].values #sorting the dataframe by Age and Name and updating the Age column accordingly

# df = df.sort_index() #sorting the dataframe by index

print(df)