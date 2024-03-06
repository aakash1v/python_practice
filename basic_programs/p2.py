'''Given two numbers, write a Python code to find the Maximum of these two numbers.

Examples: 

Input: a = 2, b = 4
Output: 4

Input: a = -1, b = -4
Output: -1'''
def find_max(a,b):
    return a if a>=b else b

a,b = 22,13

print(find_max(a,b))
print(a if a>=b else b)

maximum = lambda a,b: a if a>=b else b

print(maximum(10,12))

x = [a if a>=b else b]
print(x)

# maximum of two numbers using sorting
lst = [11,2,31,12,9,21]
lst.sort()
print('largest',lst[-1])
print('Second largest ...',lst[-2])


