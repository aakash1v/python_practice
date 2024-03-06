'''Program to find factorial of a number  '''

import math ,numpy

def factorial(n):
    if n<0:
        return 0
    
    result = 1
    for i in range(1,n+1):
        result = i *result
    return result

def factorial(n):

    return 1 if n in [0,1] else n * factorial(n-1)

# main code 
n = 5
# print(factorial(0))
# print(math.factorial(n))
x = numpy.prod([num for num in range(1,n+1)])
print(x)




