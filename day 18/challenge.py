#Instructions:
#Create a class Employee.
#__init__: Takes name and salary.
# Method work(): Prints "[Name] is working."
# Create a class Manager that inherits from Employee.
# Add a new method meeting(): Prints "[Name] is holding a meeting."

# Override the work() method: Make it print "[Name] is supervising others." (Polymorphism!).

# Test it:

# Create an Employee "Ram" (Salary 50k). Call work().

# Create a Manager "Sita" (Salary 100k). Call work() and meeting().

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")

class Manager(Employee):
    def meeting(self):
        print(f"{self.name} is holding the meeting.")

    def work(self):
        print(f"{self.name} is supervising others")

employe1 = Employee("Ram", 50000)
employe1.work()

manager1 = Manager("Sita", 100000)
manager1.work()
manager1.meeting()