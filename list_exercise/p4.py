'''Check if element exists in list in Python
The list is an important container in Python as it stores elements of all the data types as a collection. Knowledge of certain list operations is necessary for day-day programming. This article discusses the Fastest way to check if a value exists in a list or not using Python.

Example

Input: test_list = [1, 6, 3, 5, 3, 4]
            3  # Check if 3 exist or not.
Output: True
Explanation: The output is True because the element we are looking is exist in the list.'''




#Driver code
test_list = [1, 6, 3, 5, 3, 4]
imp_num = 30
# method1 using 'in'

True_value = imp_num in test_list 
# print(True_value)

# method2 using loop 
for i in test_list:
    if i ==imp_num:
        True_value = True
# print(True_value)
        
# method3 - using any() function 
result = any(item in test_list for item in test_list)
#  “Does string contain any list element: True” if duplicates exist and “Does string contain any list element: False” if there are no duplicates.
print("Does string contain any list element : " +str(result))
#--some counfusions with any...

'''#method4
 
# Initializing list
test_list = [10, 15, 20, 7, 46, 2808]
 
print("Checking if 15 exists in list")
 
# number of times element exists in list
exist_count = test_list.count(15)
print(exist_count)
# checking if it is more than 0
if exist_count > 0:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")
'''
from bisect import bisect_left ,bisect

# Initializing list 
test_list_set = [ 1, 6, 3, 5, 3, 4 ]
test_list_bisect = [ 1, 6, 3, 5, 3, 4 ]

print("Checking if 4 exists in list ( using set() + in) : ")

# Checking if 4 exists in list 
# using set() + in
'''set() -> new empty set object set(iterable) -> new set object

Build an unordered collection of unique elements.'''
test_list_set = set(test_list_set)
if 4 in test_list_set :
	print ("Element Exists")

print("Checking if 4 exists in list ( using sort() + bisect_left() ) : ")

# Checking if 4 exists in list 
# using sort() + bisect_left()
test_list_bisect.sort()
if bisect_left(test_list_bisect, 4) != bisect(test_list_bisect, 4):
	print ("Element Exists")
else:
	print("Element doesnt exist")
