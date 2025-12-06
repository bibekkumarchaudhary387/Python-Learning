#Daily Challenge: "The Even Sum Calculator"
#Challenge: Write a script that calculates the sum of all even numbers between 1 and 100 (including 100)
sum = 0
for i in range(2, 101, 2):
    sum += i
print(f"Sum of Even number upto 100 is {sum}")