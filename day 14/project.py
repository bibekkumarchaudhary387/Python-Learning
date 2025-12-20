#Create a tool that generates a secure password and saves it to a text file.

#Step 1: The Character Pool
#You need to import random and string. Use string to get a list of letters, numbers, and symbols instantly.

#Step 2: The Logic
#Combine characters: characters = string.ascii_letters + string.digits + string.punctuation
#Ask the user for the length of the password.

#Use a loop or random.sample/random.choices to pick characters.

#Step 3: The File Save
#Append the password to a file named my_passwords.txt so the user doesn't lose it.

import random
import string

use_for = input("What is this password for(eg, google): ")

char = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter length of password you want: "))
password = ""

for i in range(length):
	password = password + random.choice(char)

with open("password.txt", "a") as password_file:
	password_file.write(f"{password}\n")
print("Password Saved")