import numpy as np

#Find row-wise and column-wise sums

arr = np.array([
    [1,2],
    [3,4]
])

print(np.sum(arr, axis=0)) #row collapse

print(np.sum(arr, axis =1)) #col collapse