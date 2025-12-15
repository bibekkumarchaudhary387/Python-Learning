#Identifying Missing Features (Difference)
#Goal: Determine which features are present in one set but missing from another, which is critical for ensuring consistent data pipelines.
#Task: Find all features present in the full_feature_set that are missing from the current_data_set.

full_feature_set = {'age', 'income', 'city', 'education', 'occupation'}
current_data_set = {'age', 'income', 'city', 'gender'}

new_data_set = full_feature_set - current_data_set
print(new_data_set)