'''Write a Python program for a given multiple numbers and a number n, the task is to print the remainder after multiplying all the numbers divided by n.

Examples:

Input: arr[] = {100, 10, 5, 25, 35, 14},
n = 11
Output: 9
Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9
Input : arr[] = {100, 10},
n = 5
Output : 0
Explanation: 100 x 10 = 1000 % 5 = 0'''
from functools import reduce

def findremainder(arr,n):
    l = len(arr)
    prod =1
    for i in arr:
        prod = prod *i
    rem = prod%n
    return rem

def findremainder(arr, n):
    lens = len(arr)
    mul = 1
 
    # find the individual
    # remainder and 
    # multiple with mul.
    for i in range(lens): 
       mul = (mul *(arr[i]%n))% n
    return mul % n

def remAfterMultiplication(arr,n):
    return reduce(lambda x,y: (x*y)%n,arr)

arr = [100, 10, 5, 25, 35, 14]
n = 11
print(arr)
print(findremainder(arr, n))
print(remAfterMultiplication(arr, n))