#Consolidated Feature Set (Union)
#Goal: Create a master list of all unique features when combining multiple datasets.
#Task: Combine set_A, set_B, and set_C into a single set that contains all unique feature names.

set_A = {'model_1', 'model_2'}
set_B = {'model_2', 'model_3'}
set_C = {'model_4', 'model_1'}

master_set = set_A | set_B | set_C 
print(master_set)