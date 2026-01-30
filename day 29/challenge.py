import pandas as pd

# Scenario: You have a small dataset of student marks. You need to analyze it.
# Instructions:
# Create a DataFrame with this data:
# Name: ["Anish", "Binod", "Chanda", "Deepa"]
# Math: [85, 45, 92, 35]
# Science: [78, 56, 88, 40]
# Add a Column: Create a new column called "Total" which is df["Math"] + df["Science"].
# Filter: Create a new variable passed_students that contains only the rows where "Total" is greater than 100.
# Print the passed_students DataFrame.
# Paste your code below! This is exactly how Data

data = {
    "Name": ["Anish", "Binod", "Chanda", "Deepa"],
    "Math": [85, 45, 92, 35],
    "Science": [78, 56, 88, 40]
}

df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"]

passed_students = df[df["Total"] > 100]

print(passed_students)