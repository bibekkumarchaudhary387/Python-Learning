#The greeter Create a function called greet_user that takes a name as an input and prints "Good Morning, "[name]". Call it with your name

def greet_user(name):
	print(f"Good Morning, {name}")


name = input("Enter your name: ")
greet_user(name)
