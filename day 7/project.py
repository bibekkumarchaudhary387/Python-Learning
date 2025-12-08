#The Project PlanWe are building a game where you play against the CPU.

#Logic Flow:
#Setup: 
#Import random and create a list of choices: ["rock", "paper", "scissors"].
#Computer Turn: Make the computer pick a random option from that list.
#Player Turn: Ask the user for their input.
#The Logic (The Brain):Tie: If player == computer
#Print "It's a tie!"Win:Rock beats Scissors.Scissors beats Paper.Paper beats Rock.

import random

option = ["rock","paper","scissor"]
bot_choice = random.choice(option)
player_choice = input("Enter your choice (rock, paper or scissor): ").lower()

if bot_choice == player_choice:
	print("Its tie")
elif player_choice == "rock":
	if bot_choice == "paper":
		print("Bot win")
	else:
		print("Player win")
elif player_choice == "paper":
	if bot_choice == "scissor":
		print("Bot win")
	else:
		print("Player win")
else:
	if bot_choice == "rock":
		print("Bot win")
	else:
		print("Player win")