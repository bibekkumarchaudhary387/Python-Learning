#Categorical Data Encoding Check
#Goal: Verify if a set of collected categories fully covers the set of expected categories.
#Task: Write a function is_complete(collected_categories, expected_categories) that returns True if all expected_categories are present in collected_categories, otherwise False.

def temp_check (a, b):
    return b.issubset(a)
	
collected_categories = {'Cat', 'Dog', 'Bird', 'Fish'}
expected_categories = {'Cat', 'Dog', 'Bird'}

check = temp_check(collected_categories, expected_categories)
print(check)
