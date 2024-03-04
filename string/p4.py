'''
Strings are data types used to represent text/characters. In this article, we present different methods for the problem of removing the ith character from a string and talk about possible solutions that can be employed in achieving them using Python.

Input: 'Geeks123For123Geeks'
Output: GeeksForGeeks
Explanation: In This, we have removed the '123' character from a string.
'''
def remove_ith_char(s,i):
    if i ==0:
        return s[1:]
    
    return s[0] + remove_ith_char(s[1:],i-1)

test_str = "GeeksForGeeks"

''' 
# new_string = test_str.replace('e','o')
new_string = test_str.replace('e','',1)
print(new_string)
The major drawback of using replace() is that it fails in cases where there are duplicates in a string that match the char at pos. i. replace() replaces all the occurrences of a particular character and hence would replace all the occurrences of all the characters at pos i.'''
# translate 
# str = 'Geeks123For123Geeks'
# new_string = str.translate({ord(i): None for i in '123'})
# print(new_string)

# result = remove_ith_char(test_str,4)
# print(result)

'''new_str = ""
for i in range(len(test_str)):
    if i !=3:
        new_str +=test_str[i]
    
print ("The string after removal of i'th character : " + new_str)'''

# Removing char at pos 3
# using slice + concatenation
# new_str = test_str[:2] + test_str[3:]
# print(new_str)

# new_str = ''.join(test_str[i] for i in range(len(test_str)) if i not in [1,2,3,4,5])
# print(new_str)

# Delete Letters From a String in Python Using bytearray

'''def remove_char(s,i):
    b = bytearray(s,'utf-8')
    # print(b)
    del b[i]
    return b.decode()

print(remove_char(test_str,0))'''

lst = list(test_str)
del lst[3]
new_str = ''.join(lst)
print(new_str)

# Remove Letters From a String Using removeprefix() --remove from begning..bas..

s1 = test_str.removeprefix('G')
print(s1)
s2 = test_str[:5] + test_str[5:].removeprefix('F')
print(s2)
