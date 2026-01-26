import numpy as np

#basic sorting
arr = np.array([1,25,6,88,85,35,8,3,6])
sorted_arr = np.sort(arr)

#sorting 
arr.sort()

#sorting along axis 2d array
arr = np.array([
    [5,2,8],
    [57,20,5]
])

# print(np.sort(arr, axis=1))  #np.sort(arr, axis=1)

#indirect sorting

names = np.array(["Bibek","Sonam","Sandhya"])
grade = np.array([4,7,1])

sorrtedArr = np.argsort(grade)
# print(names[sorrtedArr])

