#Task B: What Time is it?
#Import datetime.
#Get the current time: now = datetime.datetime.now().
#Print just the year: print(now.year).
#Print the full date: print(now.strftime("%Y-%m-%d")) (This formats it like 2025-12-17).

import datetime as dt

now = dt.datetime.now()
print(now.year)

print(f"{now.year}-{now.month}-{now.day}")

print(f"{now.hour}:{now.minute}:{now.second}")