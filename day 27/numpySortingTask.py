import numpy as np

#Sort each row of a matrix
arr = np.array([
    [5,66,21],
    [83,254,20]
])

sortedArr = np.sort(arr, axis=0)
print(sortedArr)


#Find index of max element
print(f"index of max element is: {np.argmax(sortedArr)}")