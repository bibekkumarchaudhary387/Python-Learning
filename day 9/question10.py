#Goal: Find features that are unique to either set, but not shared between them (useful for highlighting differences in experimental setups).
#Task: Calculate the symmetric difference between experiment_A and experiment_B.


experiment_A = {'batch_size', 'learning_rate', 'epochs'}
experiment_B = {'regularization', 'learning_rate', 'optimizer'}

# Your code here:

main_set = experiment_A ^ experiment_B
print(main_set)