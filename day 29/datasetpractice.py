import pandas as pd

data = {
    "Name": ["Bibek", "Ram","Sita"],
    "Subject": ["DSA", "Web Tech", "SAD"],
    "Marks": [90, 85, 88]
}

df = pd.DataFrame(data)
print(df)
