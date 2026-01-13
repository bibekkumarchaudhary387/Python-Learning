import numpy as np

#Convert a 1D array of size 16 into a 4×4 matrix

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

new_array = array.reshape([4,4])

print(new_array)