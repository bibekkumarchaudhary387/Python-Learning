import numpy as np

#Extract all even numbers
number = np.arange(50)
filter_number = number[number%2 == 0]
print(filter_number)

#Replace all values > 50 with 0
a = np.array([[50,30,50,20],[50,30,503,0],[46,52,16,64],[51,50,51,56]])
a[a>50]= 0

print(a)