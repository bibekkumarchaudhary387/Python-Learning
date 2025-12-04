#Daily Challenge: "The Rollercoaster Ticket"
#Combine everything learned so far (Input, Int, If/Else).

#Rules:
#1.Ask user for their height in cm.
#2.If height is over 120 cm:
#->Print "You can ride!"
#->Ask for their age.
#->If age is under 12: Print "Ticket is $5".
#->If age is 12 to 18: Print "Ticket is $7".
#->Else (Over 18): Print "Ticket is $12".
#3.Else (Height under 120):
#->Print "Sorry, you have to grow taller."
height = float(input("Enter your height(cm): "))
if(height >= 120 ):
    print("You can Ride!")
    age = int(input("Enter your age: "))
    if(age<12):
        print("Ticket price is $5")
    elif(age>=12 and age <= 18):
        print("Ticket price is $7")
    else:
        print("Ticket price is %12")
else:
    print("You have to grow your height")