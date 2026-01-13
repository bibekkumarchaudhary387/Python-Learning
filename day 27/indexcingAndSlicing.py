import numpy as np

# a = np.array([10, 20, 30, 40])
# print(a[0])
# print(a[-1])
# print(a[1:3])

b = np.array([[1,2,3],[4,5,6]])

print(b[0, 1])      # 2
print(b[:, 1])     # column
print(b[1, :])      # row
