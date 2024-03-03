'''
Given a string. the task is to check if the string is symmetrical and palindrome or not. A string is said to be symmetrical if both the halves of the string are the same and a string is said to be a palindrome string if one half of the string is the reverse of the other half or if a string appears same when read forward or backward.

Example: 

Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome
'''
import re


# approach1
def palindrome(s):
    rev = s[::-1]
    if rev == s:
        return 'The entered string is Palindrome'
    else:
        return 'The entered string is not Palindrome'
    
def symmetrical(s):

    half =len(s)//2
    first_half = s[:half]
    second_half = s[half:]
    
    if first_half == second_half :
        return 'The entered string is symmetrical'



# aproach2 
def palindrome(s):
    mid = (len(s)-1)//2
    start = 0
    last = len(s) -1
    flag = 0

    while(start <=mid):
        if s[start] ==s[last]:
            start +=1
            last -=1
        else:
            flag =1
            break

    if flag == 0:
        return ("The entered string is palindrome")
    else:
        return ("The entered string is not palindrome")

# string is symmetrical or not 
def symmetrical(s):
    n = len(s)
    flag = 0
    if n%2: #odd 'n'
        mid = n//2 +1
    else: #if n is even..
        mid = n//2
    
    start1 = 0
    start2 = mid

    while(start1 <mid and start2 <n):
        if (s[start1] == s[start2]):
            start1 +=1
            start2 +=1
        else:
            flag =1
            break
    
    if flag == 0:
        return ("The entered string is Symmetrical")
    else:
        return ("The entered string is not Symmetrical")




def check_string(s):
    print(symmetrical(s))
    print(palindrome(s))

# Main
str1 = 'khokho'
str2 = 'amaama'

check_string(str1)
check_string(str2)
input_str = str1
    
 