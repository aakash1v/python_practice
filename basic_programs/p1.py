'''
Learn easy techniques and codes to add numbers in Python. Adding numbers in Python is a very easy task, and we have provided you 7 different ways to add numbers in Python.

Given two numbers num1 and num2. The task is to write a Python program to find the addition of these two numbers. 

Examples:

Input: num1 = 5, num2 = 3
Output: 8
Input: num1 = 13, num2 = 6
Output: 19
'''
import operator 
# Define a recursive function to add two numbers
def add_numbers_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_numbers_recursive(x + 1, y - 1)

num1,num2 = 5,3
sum = num1+num2
print(sum)
# number1 = input("First number: ")
# number2 = input("Second number: ")
# sum = float(number1) + float(number2)
# print(sum)

print(operator.add(num1,num2))
result = lambda x,y: x+y
print(result(num1,num2))
