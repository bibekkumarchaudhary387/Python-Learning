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