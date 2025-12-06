#write a program to find the largest number in a list.

count = [2,6,10,15,120]
great = 0
for x in range(len(count)):
    if count[x] > great:
        great = count[x]
print(f"Greatest value is {great}")