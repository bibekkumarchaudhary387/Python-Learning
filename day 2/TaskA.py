age = input("Enter your age: ")
salary = input("Your monhtly salary: ")
new_list = input("Enter 3 numbers (comma is compulsory): ")

age = int(age)
salary = float(salary)
final_list = new_list.split(",")
numbers = [int(x) for x in final_list]

print(f"Type of Age is {type(age)}")
print(f"Type of salary is {type(salary)}")
print(f"Type of numbers is {type(numbers)}")

anual_salary = salary * 12
sum_of_numbers = 0
for x  in numbers:
    sum_of_numbers += x

print(f"Anual Salary is {anual_salary}")
print(f"SUm of three numbers is {sum_of_numbers}")
