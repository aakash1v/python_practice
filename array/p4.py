'''Python Program for Reversal algorithm for array rotation'''

# Function to reverse arr[] from index start to end
def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
 
# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d-1) # [2,1,3,4,5,6,7] -- reverse only (0-1 index)
    rverseArray(arr, d, n-1) # [2,1,7,6,5,4,3]  -- reverse only (2-6 index)
    rverseArray(arr, 0, n-1) # [3,4,5,6,7,1,2] -- reverse the whole reversed list

 # Function to print an array
def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i],end=" ,")
    print()
 # Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)
leftRotate(arr, 2) # Rotate array by 2
printArray(arr)