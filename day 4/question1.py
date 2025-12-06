#if name is less than 3 characters long
#    name must be at least 3 characters
#otherwise if its more than 50 characters long
#    name must be a maximum of 50 characters
#otehrwise
#    name looks good
name = input("Enter your name: ")
if len(name)<3:
    print("Name must be atleast 3 characters")
elif len(name)>50:
    print("Name must be a maximum size of 50 characters")
else:
    print("Name looks good")