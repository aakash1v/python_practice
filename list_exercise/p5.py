"""n this article, let's discuss different ways to clear a list in Python. Python provides a lot of different ways to clear a list and we will discuss them in this article.

Example

Input: [2, 3, 5, 6, 7]
Output: []
Explanation: Python list is cleared and it becomes empty so we have returned empty list.
"""

list1 = [1, 2, 3]  
"""list = [6, 0, 4, 1]
print('list before clear:', list)
 
# Clearing list
list.clear()
print('list after clear:', list)
   

print("List1 before deleting is : "+ str(list1))
# deleting list using reinitialization
list1 = []
print("List1 after deleting is : "+ str(list1))

list1*=0
# Printing list2 after reinitialization
print("List1 after clearing using *=0 : "
      + str(list1))

      # deleting list1 using del
del list1[:]
print("List1 after clearing using del : " + str(list1))
"""
while(len(list1)!=0):
    list1.pop()

print("list1 after deleting using pop : ",list1)

lst = [1,2,3,4,5]
print("lst before deleting using slicing ",lst)

lst = lst[:0]
print("lst after deleting using slicing : ",lst)

