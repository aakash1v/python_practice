'''
We are given a string and we need to reverse words of a given string

Examples:

Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks  
Input : str = "my name is laxmi"
output : str= laxmi is name my '''
import re

def rev_sentence(sentence):
     words = sentence.split()
     
     reverse_sentence = ' '.join(reversed(words))

     return reverse_sentence

def rev_sentence(sentence):
     
    # find all the words in sentence
    words = re.findall('\w+', sentence)
    
    # Backward iteration over list of words and join using spaces..
    # reversed_sentence = ' '.join(words[i] for i in range(len(words)-1, -1, -1))
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

string = "geeks quiz practice code"
str2 = 'My name is laxmi'

s = string.split() #it will split the string into words and store it into list..
s = s[::-1]
print(s)

lst = []
for word in s:
    lst.append(word)

new_string = ' '.join(lst)
print(new_string)
print(rev_sentence(str2))
