"""python provides us with various ways of reversing a list. We will go through some of the many techniques on how a list in Python can be reversed.

Example: 

Input: list = [4, 5, 6, 7, 8, 9]
Output: [9, 8, 7, 6, 5, 4] 
Explanation: The list we are having in the output is reversed to the list we have in the input.
"""

import numpy as np
    
	
# Reversing a list using slicing technique
def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst
 
#Python program to reverse an array
def list_reverse(arr,size):

	if(size==1):
		return arr

	elif(size==2):
		arr[0],arr[1],=arr[1],arr[0]
		return arr
	
	#if more than two elements presents, then swap first and last numbers.
	else:
		i=0
		while(i<size//2):

	#swap present and preceding numbers at time and jump to second element after swap
			arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
	
	#skip if present and preceding numbers indexes are same
			if((i!=i+1 and size-i-1 != size-i-2) and (i!=size-i-2 and size-i-1!=i+1)):
				arr[i+1],arr[size-i-2]=arr[size-i-2],arr[i+1]
			i+=2
		return arr

   
# Reversing a list using two-pointer approach
def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
 
    return arr
 
# arr = [1, 2, 3, 4, 5, 6, 7]
# print(reverse_list(arr))
	
	
#main code


"""print(Reverse(lst))
lst = [10, 11, 12, 13, 14, 15]
arr=[1,2,3,4,5]
size=5
print('Original list: ',arr)
print("Reversed list: ",list_reverse(arr,size))

lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst)
 
print("Using reversed() ", list(reversed(lst)))"""

# input list
lst = [10, 11, 12, 13, 14, 15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = []  # empty list
 
# iterate to reverse the list
for i in lst:
    # reversing the list
    l.insert(0, i)
# printing result
# print(l)

lst = [10, 11, 12, 13, 14, 15]
n = len(lst)
reverse_list = [lst[n-i-1] for i in range(n)]
print(reverse_list)




 
# Input list
my_list = [4, 5, 6, 7, 8, 9]
 
# Convert the list to a 1D numpy array
my_array = np.array(my_list)
 
# Reverse the order of the array
reversed_array = my_array[::-1]
 
# Convert the reversed array to a list
reversed_list = reversed_array.tolist()
 
# Print the reversed list
print(reversed_list)