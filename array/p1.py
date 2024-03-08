'''Given an array of integers, find the sum of its elements.

Examples:

Input : arr[] = {1, 2, 3}
Output : 6
Explanation: 1 + 2 + 3 = 6'''
from functools import reduce
from collections import Counter

def _sum(arr):
	sum = 0

	# for i in arr:
	# 	sum = sum + i
	sum = reduce(lambda x,y :x+y,arr)
	return(sum)

def sum_of_array(arr, low, high):
	if low == high:
		return arr[low]
	mid = (low + high) // 2
	left_sum = sum_of_array(arr, low, mid)
	right_sum = sum_of_array(arr, mid+1, high)
	return left_sum + right_sum


def main():
    arr =[1,2,3,4]
    c = Counter(arr)
    # print(c.items())
    sum =0
    for key,value in c.items():
        sum = sum +key*value
    print(sum)
    # n = len(arr)
    # ans = sum(arr)
    # ans = _sum(arr)

    # print('Sum of the array is ', ans)
    # s=0
    # list1 = [12, 3, 4, 15]
    # for i,a in enumerate(list1): 
    #     s+=a 
    # print(s)
    # s=0
    # for a in list1:
    #     s+=a
    # print(s)

    #Examples
    # arr = [1, 2, 3]
    # print(sum_of_array(arr, 0, len(arr)-1)) # Output: 6

    # arr = [15, 12, 13, 10]
    # print(sum_of_array(arr, 0, len(arr)-1)) # Output: 50


# main function
if __name__ == "__main__":
	main()


