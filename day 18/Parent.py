class Vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f"Company {self.brand} model {self.model} is driving.")

class Car(Vehicle):
    def __init__(self,brand, model, number_plate):
        super().__init__(brand, model)
        self.number_plate = number_plate

    def honk(self):
        print(f"This {self.brand} company model {self.model} number is {self.number_plate}")

car1 = Car("BMW", "S-series", 2323)
car1.honk()
car1.drive()