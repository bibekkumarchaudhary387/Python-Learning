#creating the set

my_set = {"Bibek","Shandhya","Suman"}
print(my_set)

#example of dublicate in set
my_set2 = {"Bibek","Shandhya","Suman","Bibek"}
print(my_set2) #duplicate will ignored

#lenght of set
print(len(my_set2)) #number of item in set

#type of set
print(type(my_set2)) #type of set

#using set constructor
my_set3 = set(("Bibek","Shandhya","Suman"))

#access set item

set_for_loop = {1,2,3,4,5,6,6}
for x in set_for_loop:
    print(x)

print("Bibek" in set_for_loop) #check if item is present in set

#add item in set
set_for_loop.add("Bibek")
print(set_for_loop)

#add multiple item in set
set_temp = {"Bibek", "Shandhya", "Suman"}
set_for_loop.update(set_temp)

#remove item from set
set_for_loop.remove("Bibek")
print(set_for_loop)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#loop item
set_b = {1,2,3,4,5,6}
for x in set_b:
    print(x)

#join two set
set1 = {1,2,3,4,5,6}
set2 = {7,8,9,10,11,12}
#union
set3 = set1.union(set2) #joint two set completety
print(set3)
#Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#join multiple set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

#Use | :
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

#join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#intersaction
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

#using & for intersaction
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

#intersection_update
set1 = {"a", "b", "c"}
set2 = {1, "b", 3}
set1.intersection_update(set2)
print(set1)

#difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

#use - for difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

#difference_update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

#symmetric_difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

#use ^ for symmetric_difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2 
print(set3)

#symmetric_difference_update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

#isdisjoint
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "facebook"}
set3 = set1.isdisjoint(set2)
print(set3)

#issubset
set1 = {"a", "b", "c"}
set2 = {"f", "e", "d", "c", "b", "a"}
set3 = set1.issubset(set2)
print(set3)

#issuperset
set1 = {"a", "b", "c"}
set2 = {"f", "e", "d", "c", "b", "a"}
set3 = set2.issuperset(set1)
print(set3)

#copy
set1 = {"apple", "banana", "cherry"}
set2 = set1.copy()
print(set2)

#clear
set1 = {"apple", "banana", "cherry"}
set1.clear()
print(set1)

#del
set1 = {"apple", "banana", "cherry"}
del set1
print(set1) 

#create frozenset
set1 = frozenset({"apple", "banana", "cherry"})
print(set1)

#pop
set1 = {"apple", "banana", "cherry"}
set1.pop()
print(set1)

