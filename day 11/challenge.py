#Daily Challenge: "The ATM Machine (Safe Version)"
#Scenario: You are coding an ATM. You have $1000 in the bank.
#Instructions:
#Set balance = 1000.
#Ask the user: "How much do you want to withdraw?"
#The Logic:
#Wrap the logic in a try/except block.
#Convert input to int.
#If amount > balance: Raise a manual error using raise ValueError("Insufficient funds") OR just print a warning.
#Else: Subtract amount and print "Remaining balance: X".
#The Safety Net:
#except ValueError: Print "Please enter a valid number."

balance = 1000
withdraw_amount = input("How must do you want to Withdraw: ")

try:
	withdraw = int(withdraw_amount)
	if withdraw > balance:
		print("Insufficent Fund")
	else:
		print(f"Withdraw is successfull. \nRemaining Amount is {balance - withdraw}")
except ValueError:
	print("Please enter a valid number")
	