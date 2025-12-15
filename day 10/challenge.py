#Daily Challenge: "The Email Slicer"
#Scenario: You have a list of emails, and you need to separate the Username from the Domain (e.g., Gmail, Yahoo).

#Instructions:
#Ask the user for an email address (e.g., john.doe@gmail.com).
#Use the .split() method. Hint: Split by the "@" symbol.
#This will give you a list with two items: ["john.doe", "gmail.com"].
#Save the first part as username and the second part as domain.
#Print:
#"Username: [username]"
#"Domain: [domain]"
#Bonus: Make sure to .strip() the input first just in case they added spaces by accident!

email = input("Enter your email address: ")
seperate_email = email.split("@")
username = seperate_email[0]
domain = seperate_email[1]
print(f"Username: {username}")
print(f"Domain: {domain}")