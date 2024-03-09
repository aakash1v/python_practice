'''Given an array A containing n integers. The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone increasing if for all i <= j, A[i] <= A[j]. 

An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. 

Return Type: Boolean value, “True” if the given array A is monotonic else return “False” (without quotes).'''

def isMonotonic(arr):
    x, y = [],[]
    x.extend(arr)
    y.extend(arr)

    x.sort()
    y.sort(reverse=True)

    if(x==arr or y ==arr):
       return True
    else:
        return False

def isMonotonic(A):
    n = len(A)-1
    return all(A[i]<=A[i+1] for i in range(n)) or all(A[i]>=A[i+1] for i in range(n))


   

# Example usage
arr1 = [1, 2, 3, 4, 5] # True
arr2 = [5, 4, 3, 2, 1] # True
arr3 = [1, 2, 2, 3, 4] # True
arr4 = [1, 2, 3, 4, 5, 4] # False
 
print(isMonotonic(arr1)) # should return True
print(isMonotonic(arr2)) # should return True
print(isMonotonic(arr3)) # should return True
print(isMonotonic(arr4)) # should return False