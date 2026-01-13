import numpy as np #importing numpy library

#creating the array using numpy library
#1D array
array_1D = np.array([1,2,3,4])
print(array_1D)

#2D array
array_2D = np.array([[1,2],[3,4]])
print(array_2D)

#special array

#creating 3 by 3 of zero 2d array
zeroArr = np.zeros((3,3)) 
print(zeroArr)

#creating 3 by 3 of one 2d array
oneArr = np.ones((3,3)) 
print(oneArr)

#creating identity matrix
eye = np.eye(3)
print(eye)

#creating range
print(np.arange(0,10,5))

print(np.linspace(0,1,5))