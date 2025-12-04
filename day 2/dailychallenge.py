#Daily Challenge: The Age Calculator
#Goal: Ask the user for their birth year, and tell them how old they are.
#The Trap: input() ALWAYS returns a String. Even if I type 2000, Python saves it as "2000" (text). You cannot subtract text from a number (2025 - "2000" = Error). You must cast it.

#Instructions:
#Use input() to get the birth year.
#Convert that input into an int.
#Calculate age (Current Year - Birth Year).
#Print the result.

bday = input("Enter your birthyear (BS): ")
bday = int(bday)
age = 2082-bday
print("You are",age,"years old")