import numpy as np
data = np.array([10, -5, 20, -1, 30])

# Find all negative numbers and set them to 0
data[data < 0] = 0

print(data) # Output: [10, 0, 20, 0, 30]