import pandas as pd

# creating the data frames
data = {
    "name": ["Bibek", "Dickshit", "Anish", "Praman"],
    "age": [22, 23, 21, 24],
    "city": ["Barju","Kathmandu", "Lalitput", "Pokhara"],
    "marrks": [90, 34, 67, 99]
}

df = pd.DataFrame(data)

print(df)

# accessing specific columns
# print(df["name"])
# print(df["age"])
# print(df["city"])
# print(df["marrks"])
# accessing specific rows
# print(df.iloc[0])  # accessing by position
# print(df.loc[1])   # accessing by index label

# accessing specific values
print(df.at[2, "name"])  # accessing by index label and column