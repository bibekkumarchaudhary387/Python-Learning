# Base Class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}"

    def calculate_annual_salary(self):
        return self.salary * 12     # You can make it *13 if needed


# Derived Class - Manager
class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    # Method overriding
    def get_details(self):
        return (f"Name: {self.name}, ID: {self.employee_id}, "
                f"Department: {self.department}")


# Derived Class - Developer
class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def get_language(self):
        return self.programming_language


# ---------- Testing the Classes ----------

# Creating objects
manager = Manager("Bibek", 101, 200000, "HR")
developer = Developer("Sonam", 102, 500000, "Python")

# Printing details
print("Manager Details:", manager.get_details())
print("Developer Details:", developer.get_details())

# Developer specific
print("Developer Language:", developer.get_language())

# Annual Salaries
print("Annual Salary of Manager:", manager.calculate_annual_salary())
print("Annual Salary of Developer:", developer.calculate_annual_salary())
