# extended weight converter
weight = int(input("Enter your weight: "))
ans = input("you entered (K)g or (P)ound: ")
if ans == 'k' or ans == 'K':

    print("your weight in pound is:", weight * 2.20462,"pound")
elif ans == 'p' or ans == 'P' :
    print("Your weight in kg is:",weight/2.20462,"kgs")
else:
    print("Wrong input")