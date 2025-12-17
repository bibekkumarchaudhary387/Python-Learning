#Daily Challenge: "The Dice Simulator"
#Scenario: You are playing a board game (Ludo!) and lost the dice. You need a program to roll for you.

#Instructions:
#Import the random module.
#Create a while True: loop.
#Inside the loop:
#Ask input: "Press Enter to roll (or type 'quit' to exit): ".
#If they type 'quit', break.
#Generate a random integer between 1 and 6 using random.randint(1, 6).
#Print: "You rolled a [number]! 🎲".
#Bonus: If they roll a 6, print "Wow! You get another turn!"

import random as ludo

while True:
	user = input("Press Enter to roll (or type 'quit' to exit): ")
	
	if user == "quit".lower:
		break
	
	dice = ludo.randint(1,6)
	print(f"You rolled a {dice}! 🎲")

	if dice == 6:
		print("Wow! You get another turn!")
	