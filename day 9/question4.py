#Goal: Identify features common to two different feature sets, such as overlapping features between a training set and a validation set.

#Task: Find the common features between train_features and validation_features. Print the resulting set.

train_features = {'age', 'income', 'city', 'occupation', 'gender'}
validation_features = {'city', 'income', 'education', 'age'}

print(f"Common item are: {train_features & validation_features}")