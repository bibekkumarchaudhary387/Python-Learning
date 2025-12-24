class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sound(self):
        print(f"{self.name} is you, And your age is {self.age}")

class Me(Employee):
    def to(self):
        print("Thiss is called real inheritence")

p1 = Employee("Bibek", 22)
p1.sound()
p2 = Me("Ram",45)
p2.to()