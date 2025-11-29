#wap to find the greatest of 3 numbers entered by the user
var1 = int(input("Enter 1st value: "))
var2 = int(input("Enter 2nd value: "))
var3 = int(input("Enter 3rd value: "))
if(var1 > var2 and var1 > var3):
    print(var1,"is greatest")
elif(var2 > var3):
    print(var2, "is greatest")
else:
    print(var3, "is greatest")