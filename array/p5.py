'''Python Program to Split the array and add the first part to the end'''
from collections import deque

def splitArr(arr,k):
    n = len(arr)
    for i in range(0,k):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp

   
# Python program to split array and move first
# part to end.
 
 
def splitArr(a, k):
    x = a[:k] #sub array from a 
    y = a[k:]
    y.extend(x)
    return y
 
   
 
def splitArr(a, k):

  q = deque(a)
  q.rotate(-k)
  return list(q)
 
# main
arr = [12, 10, 5, 6, 52, 36]
print(arr)
n = len(arr)
position = 2
# splitArr(arr, position)



arr = splitArr(arr, position)
print(arr)



