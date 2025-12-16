#Task B: The Index Guard Create a list: fruits = ["Apple", "Banana"]. Ask the user for an index number. Use try/except to handle the IndexError if they ask for index 5 (which doesn't exist).

fruits = ["Apple","Banana"]

num = input("Enter a index for print: ")

try:
	real_num = int(num) 
	print(fruits[real_num])
except IndexError:
	print("Index doesnot exist")	


