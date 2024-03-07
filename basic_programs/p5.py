'''
Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
Example:

Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9'''

# Function to calculate x raised to 
# the power y
# def power(x, y):
     
#     if y == 0:
#         return 1
#     if y % 2 == 0:
#         return power(x, y // 2) * power(x, y // 2)
         
#     return x * power(x, y // 2) * power(x, y // 2)

# Function to calculate order of the number simply checking numbers of digits...
'''def order(x):
 
    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
         
    return n

# Function to check whether the given 
# number is Armstrong number or not
def isArmstrong(x):
     
    n = order(x)
    temp = x
    sum1 = 0
     
    # while (temp != 0):
    #     r = temp % 10
    #     sum1 = sum1 + r**n #power(r, n)
    #     temp = temp // 10
    
    for i in range(n):
        r = temp %10
        sum1 = sum1+ r**n 
        temp = temp//10
        
    return (sum1 == x)
 
# Driver code
x = 153
print(isArmstrong(x))
 
x = 1253
print(isArmstrong(x))'''

 
n = 153  # or n=int(input()) -> taking input from user
s = n  # assigning input value to the s variable
b = len(str(n)) # give u the order or number of digits..
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")


   
def is_armstrong_number(number):
    return sum(int(digit)**len(str(number)) for digit in str(number)) == number

print(is_armstrong_number(n))


