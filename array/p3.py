'''Python Program for Array Rotation'''

# Python program to left-rotate the given array

def reverse(start, end, arr):

	# No of iterations needed for reversing the list
	no_of_reverse = end-start+1

	# By incrementing count value swapping of first and last elements is done.
	count = 0
	while((no_of_reverse)//2 != count):
		arr[start+count], arr[end-count] = arr[end-count], arr[start+count]
		count += 1
	return arr

def left_rotate_array(arr, size, d):

	# Reverse the Entire List
	start = 0
	end = size-1
	arr = reverse(start, end, arr) #[8,7,6,5,4,3,2,1]

	# Divide array into twosub-array
	# based on no of rotations.
	# Divide First sub-array
	# Reverse the First sub-array
	start = 0
	end = size-d-1
	arr = reverse(start, end, arr)  #[3,4,5,6,7,8,2,1]

	# Divide Second sub-array
	# Reverse the Second sub-array
	start = size-d
	end = size-1
	arr = reverse(start, end, arr) #[3,4,5,6,7,8,1,2]
	return arr

# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    #at this time temp =[1,2]
    while (d < n):
        arr[i] = arr[d]  #good:)
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp #it is like [3,4,5,6,7,8]  + [1,2]
    return arr

# Driver code 
arr = [1, 2, 3, 4, 5, 6, 7, 8]
size = 8
d = 2
print('Original array:', arr)

# Finding all the symmetric rotation number
# if(d <= size):
# 	print('Rotated array: ', left_rotate_array(arr, size, d))
# else:
# 	d = d % size
# 	print('Rotated array: ', left_rotate_array(arr, size, d))

# This code contributed by SR.Dhanush
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))