import numpy as np

#creating the generator
rng = np.random.default_rng()

#Generate a random 5×5 matrix
arr = rng.integers(low=0, high=100, size=(5,5))
print(arr)

#Find max value and its index
print(f"Min Value: {np.min(arr)}")
minindex = np.argmin(arr)
print(f"min index: {minindex}")

print(f"Max Value: {np.max(arr)}")
maxindex = np.argmax(arr)
print(f"min index: {maxindex}")