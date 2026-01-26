import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print("---vstack---")
print(np.vstack((arr1, arr2)))
print("---hstack---")
print(np.hstack((arr1, arr2)))

#spiliting

#horizontal and vertical spiliting
sarr1 = np.array([
    [1,2,3,4],
    [6,7,8,9]
])

split_arr =np.hsplit(sarr1,2)
# print(split_arr[0])

#spit at specific part
newarr = np.array([1,2,3,4,5,6,7,8,9])
specificarr = np.split(newarr, [2,6])
print(specificarr)