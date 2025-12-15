#Goal: Find all unique feature names from a set of collected data samples.
data_features = [
    ['age', 'income', 'city'],
    ['income', 'city', 'education', 'age'],
    ['city', 'occupation', 'income']
]

data_set = set()

for features in data_features:
    data_set.update(features)

print(data_set)