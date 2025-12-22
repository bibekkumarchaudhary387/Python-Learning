class Car:
	def __init__ (self,brand, color):
		self.brand = brand
		self.color = color

	def drive(self):
		print(f"The {self.color} {self.brand} is driving")

car_1 = Car("Tesla","Red")
car_1.drive()

car_2 = Car("Toyota","Blue")
car_2.drive()