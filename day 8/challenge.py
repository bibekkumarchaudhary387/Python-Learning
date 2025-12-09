#Daily Challenge: "The Simple Phonebook"
#Scenario: You want to build a contact list where you can type a name and get the number instantly.

#Instructions:
#Create a dictionary called phonebook with 3 friends and their numbers.
#Example: "Ram": 9800000000, "Sita": 9811111111
#Ask the user: "Who do you want to call?"
#Check if the name exists in the dictionary (Use if name in phonebook:).
#If yes: Print "Calling [Name] at [Number]..."
#If no: Print "Contact not found."

phonebook = {
	"bibek": 9824396787,
	"anish": 9704527011,
	"praman": 980123456
	}
name = input("Who do you want to call? ").lower()
if name in phonebook:
	print(f"Calling {name} at {phonebook[name]}...")
else:
	print("Contact not found")