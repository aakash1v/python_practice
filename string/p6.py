'''This article will cover how to check if a Python string contains another string or a substring in Python. Given two strings, check whether a substring is in the given string. 

Input: Substring = "geeks" 
        String="geeks for geeks"
Output: yes
Explanation: In this, we are checking if the substring is present in a given string or not.
'''
import re
def check(s2,s1):
    if (s2.count(s1) > 0):
        print('yes')
    else:
        print('no')

def is_substring(string,sub_string):
    flag = False
    for i in range(len(string)-len(sub_string)):
        if string[i:len(sub_string)+i] == sub_string:
            flag = True

    return flag 



Substring = "geeks" 
String="geeks for geeks"

# if Substring in String :
if String.find(Substring) != -1:
    print('yes')
else:
    print('no')

s2 = String
s1 = Substring
# check(s2,s1)

# print('yes' if s1 in s2 else 'no')

# x=list(filter(lambda x: (s1 in s2),s2.split())) 
# print(x)
# print(["yes" if x else "no"])
'''a = ['Geeks-13', 'for-56', 'Geeks-78', 'xyz-46']
for i in a:
	if i.__contains__("Geeks"):
		print(f"Yes! {i} is containing.")

if (is_substring(s2,s1)):
    print('yes')
else:
    print('no')'''

# if re.search('hello' ,'hello world !!'):
#     print('yes')
# else:
#     print('no')
import operator
print('yes' if operator.contains(s2,s1) else 'no')

