import numpy as np

# Create the generator
rng = np.random.default_rng()

# # Generate 5 random floats between 0.0 and 1.0
# print(rng.random(5))

#random integer

int_random = rng.integers(low=0, high=10, size=(2,3))

# print(int_random)


# Generate 1000 numbers from a normal distribution
samples = rng.standard_normal(1000)

# print(samples)

#shuffle and choice

arr = np.array([1, 2, 3, 4, 5])

# Shuffle the array in place
rng.shuffle(arr)

# Pick 2 random elements from the array
choice = rng.choice(arr, size=2, replace=False)

# print(choice)
# print(arr)

#reproductivity with seed

# Providing the number 42 ensures the "random" numbers are the same every run
rng = np.random.default_rng(seed=42)
print(rng.random(3)) # Will always output the same 3 numbers