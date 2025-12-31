class Employee:
    def __init__(self, name, age, base_salary):
        self.name = name
        self.age = age
        self.base_salary = base_salary

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def calculate_annual_salary(self):
        return f"{self.base_salary * 12}"
    
    def is_eligible_for_insurance(self):
        return True

class Fullemployee(Employee):
    def __init__(self, name, age, base_salary, bonus):
        super().__init__(name, age, base_salary)
        self.bonus = bonus
    
    def calculate_annual_salary(self):
        return f"{self.base_salary * 12 + self.bonus}"
    
    def is_eligible_for_insurance(self):
        return True

class PartTimeEmployee(Employee):
    def __init__(self, name, age,base_salary, hours_per_day, rate_per_hour):
        super().__init__(name, age, base_salary)
        self.hours_per_day = hours_per_day
        self.rate_per_hour = rate_per_hour
    
    def calculate_annual_salary(self):
        return f"Anual Salary: {self.hours_per_day * self.rate_per_hour * 365}" 
    
    def is_eligible_for_insurance(self):
        return False
    

emp1 = Fullemployee("Bibek", 22, 18000, 5000)
emp2 = PartTimeEmployee("Sumit", 21, 0,8, 150)

print(f"FullTime Employee Detail: \n {emp1.get_details()}")
print(f"Annual Salary: {emp1.calculate_annual_salary()}")

print(f"Part Time Employee \n Employee Detail: {emp2.get_details()}")
print(f"Anual Salary: {emp2.calculate_annual_salary()}")