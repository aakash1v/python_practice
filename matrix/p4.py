'''Python | Matrix Product'''
from itertools import chain
def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res
 
def multiply_nested_list(nested_list):
    res = 1
    for i in nested_list:
        if isinstance(i, list):
            res *= multiply_nested_list(i) #PRODUCT OF SUBLIST..
            # print(res)
        else:
            res *= i
    return res
 
# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
 
# printing original list
print("The original list : " + str(test_list))
 
# using list comprehension + loop
# Matrix Product
# lst = [elem for sub in test_list for elem in sub]
# chain_obj = chain(*test_list)

# result = prod(chain_obj)

# x = []
# for i in test_list:
#     x.extend(i)

# res = 1
# for j in x:
#     res *= j
 
# print("The total element product in lists is : " + str(res))
print(multiply_nested_list(test_list))
'''
lst = [[1,2,3],[3,4,5],[3]]
lst = "This is string."
lst = (1,2,33)
# lst = list(lst)
# print(lst)
for i in lst:
    print(isinstance(i,int))'''
