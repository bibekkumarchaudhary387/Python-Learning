# Create a program that:
# Takes input:
# Name
# Age
# Address
# Hobby

# Prints a formatted intro like:

# ----- Personal Information -----
# Name: Bibek Kumar Chaudhary
# Age: 21
# Address: Biratnagar, Nepal
# Hobby: Coding and Designing
# --------------------------------

name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
hobby = input("Enter your hobbies: ")
print("----- Personal Information -----")
print("Name:",name)
print("Age:",age)
print("Address:",address)
print("Hobby:",hobby)
print("--------------------------------")