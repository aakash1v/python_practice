# initilizing list 
'''
test_list = [1 ,20,34,400,2808,7]

print("Check if 34 exists in the list")

x = list(map(str,test_list)) #it converts all the element of the list into string..
y = '-'.join(x)
print(y)
if y.find('34') != -1:
    print('yes, 34 exists in the list ')
else:
    print('no ')
'''
from collections import Counter
 
test_list = [10, 15, 20, 7, 46, 2808]
 
# Calculating frequencies
frequency = Counter(test_list)
 
# If the element has frequency greater than 0
# then it exists else it doesn't exist
if(frequency[15] > 0):
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")

# method3

def element_exists(lst, element):
  # Try to get the index of the element in the list
  try:
    lst.index(element)
  # If the element is found, return True
    return True
  # If a ValueError is raised, the element is not in the list
  except ValueError:
  # Return False in this case
    return False
 
#Test the function
test_list = [1, 6, 3, 5, 3, 4]
 
print(element_exists(test_list, 3)) # prints True
print(element_exists(test_list, 7)) # prints False