#Task B: The Reader Write a script that opens my_name.txt, reads the text, and prints "The file says: [content]".

with open("my_name.txt", "r") as file:
	content = file.read()
	print(content)
