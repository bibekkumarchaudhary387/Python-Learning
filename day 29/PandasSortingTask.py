import pandas as pd

data = {
    "Name": ["Bibek", "Ram", "Sita", "Hari", "Gita", "Laxman", "Shyam", "Rita", "Suman", "Kiran"],
    "Subject": ["DSA", "Web Tech", "SAD", "English", "DBMS", "OS", "CN", "SE", "ML", "AI"],
    "Marks": [90, 85, 93, 88, 92, 80, 99, 95, 89, 84]
}

df= pd.DataFrame(data)

df["Marks"] = df.sort_values(by="Marks", ascending=False)["Marks"].values #sorting the dataframe by Marks and updating the Marks column accordingly

print(df)