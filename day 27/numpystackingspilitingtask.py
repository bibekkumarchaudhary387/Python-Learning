import numpy as np

#Stack two 2×2 matrices vertically

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
stackArr = np.vstack((arr1, arr2))
print(stackArr)

#Split an array into 3 equal parts
a = np.arange(9)
spitArr = np.split(a, [3,6])
print(spitArr)