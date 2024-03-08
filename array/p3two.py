def leftRotateByOne(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1]= temp

def leftRotate(arr,d):
    for i in range(d):
        leftRotateByOne(arr)
    
def printArray(arr):
    for i in arr:
        print(i ,end=' ')
    print()

def reverse(arr):
    n = len(arr)
    iteration = n//2
    i =0
    while(i != iteration):
        arr[i] ,arr[n-1-i] = arr[n-1-i],arr[i]
        i +=1    
    return arr

def rotate(arr,d):
    n = len(arr)
    arr[:] =arr[d:] + arr[:d]
    return arr
'''Python Program for Array Rotation Using 4 Juggling Algorithm'''
 
# Function to left rotate arr[] of size n by d
def leftRotate(arr, d, n):
    for i in range(gcd(d, n)): #(2)
 
        # move i-th values of blocks
        temp = arr[i]
        j = i # first :0 , second :1 
        while 1:
            k = j + d # k = 0 + 2 , 1+2 .....
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k #  first : 2 , second : 3
        arr[j] = temp  #at 2 index  ok


def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")
 
# Function to get gcd of a and b
 
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    

# Driver program to test above functions */
arr = [1, 2, 3, 4, 5, 6, 7]
# leftRotate(arr, 2)
# printArray(arr)
# print("Reversing the list by my brand new Functioin ",reverse(arr))
# print(rotate(arr,2))
leftRotate(arr, 2, 7)
printArray(arr, 7)



