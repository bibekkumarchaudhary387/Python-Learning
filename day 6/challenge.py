#Daily Challenge: "The Shopping Cart"
#Scenario: You are building a simple Amazon cart.

#Instructions:
#Create an empty list: cart = [].
#Create a while True: loop (an infinite loop).
#Inside the loop:
#Ask the user: "Enter item to buy (or type 'done' to finish): "
#If they type "done": break the loop.
#Else: .append() the item to the cart and print "Item added!".
#After the loop breaks, print: "Your final cart contains:" and print the list.

cart =[]
num = 1
while num > 0:
	item = input("Enter item to buy (or type 'done' to finish): ")
	if item != 'done' :
		cart.append(item)
	else:
		break
print("Your item list:")
print(cart)