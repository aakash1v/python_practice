'''To find the largest element in an array, iterate over each element and compare it with the current largest element. If an element is greater, update the largest element. At the end of the iteration, the largest element will be found.

Given an array, find the largest element in it.

Input : arr[] = {10, 20, 4}
Output : 20
Input : arr[] = {20, 10, 20, 4, 100}
Output : 100
'''
from functools import reduce
import operator

def largest(arr, n):
    max = arr[0]
    for i in range(n):
        if arr[i]>max:
            max = arr[i]
    return max
 
 
# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
# Ans = largest(arr, n)
# Ans = max(arr)
# arr.sort()
# Ans = arr[-1]

# Ans = reduce(max,arr)
# print("Largest in given array ", Ans)

# max =0
# for i in arr:
#     if operator.gt(i,max):
#         max = i
# print(max)
largest_element = max(arr,key=lambda x:x)
print(largest_element)

