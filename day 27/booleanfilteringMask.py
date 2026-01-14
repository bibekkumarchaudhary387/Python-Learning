import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Condition: Where is the value greater than 25?
apple = arr > 25

print(apple) 
# Output: [False False  True  True  True]

#apply the mask

filter_of_mask = arr[apple]

print(filter_of_mask)


#filtering

arr = np.array([1, 5, 10, 15, 20])

# Select values greater than 5 AND less than or equal to 15
result = arr[(arr > 5) & (arr <= 15)]

print(result) # Output: [10 15]