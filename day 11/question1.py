#Task A: The Safe Converter Write a loop that asks for a number and prints it squared. If the user types text (like "ten"), print "Please enter a digit" instead of crashing.

while True:
	num = input("Enter any value: (type exit for end the program): ")
	

	if num.lower() == 'exit':
		break

	try:
		real_num = int(num)
		print(f"The Square of {real_num} is {real_num * real_num}.")
	except ValueError:
		print("Enter int not other data type")
