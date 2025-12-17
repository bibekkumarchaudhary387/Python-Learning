#Task C: The List Saver You have a list: friends = ["Ram", "Sita", "Hari"]. Loop through the list and write each name on a new line in friends.txt. Hint: Remember to add \n after each name!

friends = ["Ram", "Sita", "Hari"]
with open("friends.txt", "w") as file:
	for i in friends:
		file.write(f"{i}\n")

