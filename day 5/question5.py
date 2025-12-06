#Create a function called square_number that takes a number, multiplies it by itself, and returns the result.

def square_number(number):
	return number*number


num = int(input("Enter any value: "))
print(f"Square of number is: {square_number(num)}")