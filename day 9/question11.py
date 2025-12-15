#Filtering Noise Data
#Goal: Remove 'noisy' or irrelevant data points from a primary dataset based on a predefined noise set.
#Task: Given data_points and noise_set, create a new set containing only the valid data points.


data_points = {10, 25, 42, 99, 5, 25, 101, 55}
noise_set = {5, 10, 101, 25}

new_set = data_points.difference(noise_set)
print(new_set)