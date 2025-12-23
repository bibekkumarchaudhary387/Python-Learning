1. 

2. 

3. 

Control flow (Making decision)
Goal: learn if, else and logical operators
* Equals : ==
Not Equals: !=
Greater/less : >,<.<=,>=
structure:
age = 20
if age>=18:
    print("You are young")
else:
    print("You are minor")

4. 

a. The for loop use this when you know how many times you want to repeat somthing. We often use it with range()

range(start, start) - stop is not included!
This prints 1, 2, 3, 4 (It stops before 5)
for number in range(1, 5):
    print(number)

b. The while loop use this when you want to loop as long as a condition is True.

count = 0
while count < 3:
    print("Loading...")
    count += 1 #crucial! if you forget this, the loop runs FOREVER (Infinite loop)

5. 

Functions (The "DRY" Principle)

Today goal: Stop writing the same code twice. DRY principle: Don't Repeat Yourself

What is functions?
A function is a block of code that only runs when you call it. Think of it like a "Recipe". You write the recipe once, but you can cook the meal as many times as you want.

The syntax:
--> def : tells python you are making a function
--> return : sends the answer back to the main program

1. Defining the function (The recipe)
    def my_greeting(name):
        print(f"Hello, {name}!")

2. Calling the function (cooking)
    my_greeting("Alice")
    my_greeting("Bob")

Return vs. Print (crucial concept)
--> print : just shows text on the screen. The computer "forgots" the value immediatly
--> return : gives the value back to the code so you can store it in a variable

    def add_numbers(a, b):
        return a + 
    
    result = add_numbers(5, 10): #request now holds 15
    print(result)

6. 

List (Storing  multiple items)

Goal: Move beyong single variable up until now if you wanted to store 5 names, you needed name1, name2, name3..., this us messy. Today, we use list to store them all in one place.

A list []
--> A list is an ordered collection of items you can chaneg it (add/remove items) anytime.

#A list of fruits
fruits = ["Apple", "Banana", "Cherry"]

#python counts from 0
print(fruits[0]) #print "Apple"
print(fruits[1]) #print "Banana"
print(fruits[-1]) #print "cherry" (negative indexing)

Modifying the list:
--> Add item: fruits.append("Orange") --> add to the end
--> Remove item: fruits.pop() --> remove the last one
--> Insert item: fruits: fruits.insert(1, "Mango") --> puts mango at index 1

Tuple
--> A tuple is a "Locked list", once you created it, you cannot change it. Use this for data that shouldn't change (like coordinates or drag of the web)

coordinates = (10,20)
#coordinates[0] = 15 <-- ERROR! you can't change tuple

7. 

8. 

Dictioaries: (Key Value Pairs)

Goal: Store data like professional. Lists ([]) are great for ordered items, but they are bad for lebelled data. If you have a user profile, you don't want to remember that index 0 is the name and index 1 is the email. You want to lebel them.

The Dictioaries {}
-->A dictioaries is a collection of keys and values.
 key: The label (likes word in book)
 value: The data (likes the definition)

 Syntax
    key on the left: value on the right

    user = {
        "name": "Alex",
        "age": 25,
        "is_student": True
    }

    Accessing data (use the key, not a number)
    print(user["name"]) --> print Alex
    print(user["age]) --> print 25

    Modifying Dictioaries
    1. Changing a value
    user["age"] = 26

    2. Adding a new key - value Pairs
    user["city"] = "kathmandu"

    3. Checking if a key exists
    if "email" in user:
        print(user["email"])
    else:
        print("No email found")

9. 

10. 

11. 

12. 

13. 

14. 

15. 

List Comprehensions (Python Shortcuts)

goal: learn how to do in one line what used to take four lines. Python is famous for being "concise". List comprehensions are the most common way to professional pythonistas write code.

The One-Liner

#Imagine you want to create a list of sqaures for numbers 1 to 5.
The Old way (4 lines):
    squares = []
    for x in range(1, 6):
        squares.append(x*x)
The New way (1 line):
    squares = [x*x for x in range(1,6)]

The syntax: [expression for item in iterable if condition]

16. 

Object-Oriented Programming (OOP) - part 1

goal: Stop thinking in "lines of code" ans start thinking in "Objects". This is the single most important concept in modern programming. In the real world, everything is an Object (a Car, a User, a Bank Account).

An Object has:
 1. Attributes (Data): What it is (e.g., color, balance, name).
 2. Methods (Actions): What it does (e.g., drive, withdraw, login).

The Class (The Blueprint)
-> A Class is the blueprint for the obeject.

The __init__ method: This is a special function that runs automatically when you create a new object. It sets up the starting data

The self keyword: self represent the specific object you are working with.

    Example:

    class Dog:
        # The contructor (Blueprint Setup)
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed

        # A method (action)
        def bark(self):
            print(f"{self.name} says: woof! woof!")
    #creating an "Instance" (making the actual dog)
    my_dog = Dog("Sheru", "Bhote Kukur")
    print(my_dog.name)
    my_dog.bark()

Practical Question

Create day16.py.

Task A: The Car Creator
1. Create a class called Car.
2. In __init__, give it attributes: brand and color.
3. Create a method called drive that prints: "The [color] [brand] is driving!"
4. Create two different cars (e.g., a Red Tesla and a Blue Toyota) and make them both drive.

17. 

Object-Oriented Programming (OOP) - Part 2

goal: Change the object's data. Yesterday, we just read data (self.name). Today, we modify it. This is the heart of software engineering: objects that change over time (like a user's bank balance changing when they buy something).

example,

    class Counter:
    def __init__(self):
        self.count = 0  # Starts at 0

    def click(self):
        self.count += 1 # Adds 1 to the specific object's count
        print(f"Click! Count is now: {self.count}")

my_clicker = Counter()
my_clicker.click() # Prints 1
my_clicker.click() # Prints 2