import numpy as np

image = np.random.randint(100, 200, (3, 3))

print("Original Image:\n", image) 

darkened_image = image - 50

final_image = np.clip(darkened_image, 0 , 255)

print("Final Image after Clipping:\n", final_image)