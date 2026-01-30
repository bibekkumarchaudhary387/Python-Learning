import pandas as pd

# 1. Create a Dictionary of data
data = {
    "Name": ["Bibek", "Ram", "Sita", "Hari", "Gita", "Laxman", "Shyam", "Rita", "Suman", "Kiran"],
    "Age": [25, 30, 28, 22, 24, 27, 29, 23, 26, 31],
    "City": ["Kathmandu", "Pokhara", "Lalitpur", "Biratnagar", "Dharan", "Hetauda", "Butwal", "Janakpur", "Nepalgunj", "Dhangadhi"],
    "Marks": [85, 90, 78, 88, 92, 80, 76, 95, 89, 84],
    "Grade": ["A", "A+", "B", "A", "A+", "B", "C", "A+", "A", "B"],
    "Passed": [True, True, True, True, True, True, False, True, True, True],
    "Height_cm": [170, 175, 160, 180, 165, 172, 168, 158, 174, 169],
    "Weight_kg": [70, 75, 60, 80, 65, 72, 68, 58, 74, 69],
    "Hobby": ["Reading", "Traveling", "Cooking", "Sports", "Music", "Art", "Gaming", "Dancing", "Photography", "Writing"],
    "Favorite_Color": ["Blue", "Green", "Red", "Yellow", "Purple", "Orange", "Pink", "Black", "White", "Gray"]
}

df = pd.DataFrame(data)

print(df.shape)
print(type(df))