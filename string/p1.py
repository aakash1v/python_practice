'''Given a string, write a python function to check if it is palindrome or not. A string is said to be a palindrome if the reverse of the string is the same as the string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

Examples: 

Input : malayalam
Output : Yes

Input : geeks
Output : No
'''
def palindrome(word):
    n = len(word)

    for i in range(n//2):
        if word[i] != word[n-i-1]: 
            check = False
    if check == True:
        print('yes')
    else:
        print('No')


def ispalindrome(word):
    return word == word[::-1]

def ispalindrome(s):
    rev = reversed(s) #create a reversed object 
    rev = ''.join(rev) #convert it into a string.
    
    if s ==rev:
        return ('Yes')
    else:
        return ('No')

def ispalindrome(s):
    w = ""
    for i in s:
        w = i+w
    
    if w ==s:
        return ('yes')
    else:
        return 'No'

'''Recursion function to check if the string is palindrome ..'''
def res_palindrome(s):
    s = s.lower()
    l = len(s)

    if l<2:
        return True
    elif s[0] == s[l-1]:
        return res_palindrome(s[1:l-1])
    else:
        return False
    
# MAIN
word = 'malayalam'
word2 ='greeks'

print(res_palindrome(word))
print(res_palindrome(word2))

# another method 
'''flag = True
j = -1
for char in word:
    if char !=  word[j]:
        flag = False
        break
    j = j-1

if flag:
    print('yes')
else:
    print('No')
    '''




