import numpy as np

list_item = [0.5, 0.8, 1.2, 0.3, 0.9]

np_array = np.array(list_item)

np_array = np_array + 0.1

print(np_array[np_array>1.0])