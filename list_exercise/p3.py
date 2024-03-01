'''How To Find the Length of a List in Python
List being an integral part of Python programming has to be learned by all Python users and having a knowledge of its utility and operations is essential and always a plus.

Many operations are performed in lists, but in this article, we will discuss the length of a list. The length of a list means the number of elements it has. We are going to look at 8 different methods to find the length of a list in Python.

Example:

Input: lst = [10,20,30,40]
Output: 4
Explanation: The output is 4 because the length of the list is  4.
'''
from operator import length_hint
from collections import Counter

def find_len(list):
    count = 0
    for i in list:
        count +=1
    return count

def count_elem_recursion(list):
    count = 0
    
    # base condition if list is not empty
    if not list:
        print('recursive approach')
        return 0
    # Recursive case: add 1 to the count of the remaining elements in the list
    return 1 + count_elem_recursion(list[1:])
    

# driver code 
lst = [10,20,30,40]
test_list = [1, 4, 5, 7, 8]
# n = len(lst)
# n = find_len(lst)

# Printing test_list
print("The list is : " + str(test_list))
# n = length_hint(test_list)
# n = sum(1 for i in test_list)

'''Calculate the length of the list using a list comprehension and the sum function
The list comprehension generates a sequence of ones for each element in the list
The sum function then sums all the ones to give the length of the list'''
# length = sum(1 for _ in test_list)

# length = count_elem_recursion(test_list)
# print("The length of the array is ",length)

'''s = 0
for i, x in enumerate(lst):
    s +=1
print(s)'''

list_len = sum(Counter(test_list).values())
print("The length using Counter() class ",list_len)
