import pandas as pd

students = pd.Series([88, 92, 79, 95, 85], index=["Alice", "Bob", "Charlie", "David", "Eva"])
heighest_mark = students.max()

print("Heighest Mark:", heighest_mark)

#print the student with the heighest mark
top_student = students.idxmax()
print("Top Student:", top_student)