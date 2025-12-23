class Student:
	name = "Bibek"
	grade = 85
	
def is_passing(self):
        if self.grade >= 40: 
                return True
        else:
                return False   

stu1 = Student()
stu2 = Student()
stu2.name = "Anish"
stu2.grade = 35
print(f"{stu1.name} is Passed with Grade {stu1.grade}" if is_passing() else "Fail")
print(f"{stu2.name} is passed with {stu2.grade} grade" if is_passing() else "Fail")