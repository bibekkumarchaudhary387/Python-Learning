class Student:
	def __init__(self,name,grade):
		self.name = name
		self.grade = grade
	
	def is_passing(self):
		if self.grade >= 40: 
			return True
		else: 
			return False

student1 = Student("Bibek", 85)
passstu = student1.is_passing()
print(f"{student1.name} Passing: {student1.grade}" if passstu else "Fail") 

student2 = Student("Anish",35)
passstu = student2.is_passing()       
print(f"{student2.name} Passing: {student2.grade}" if passstu else "Fail")



