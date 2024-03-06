'''Sometimes while working with Python strings, we can have a problem in which we need to extract the frequency of all the words in a string. This problem has been solved earlier. This discusses the shorthands to solve this problem as this has applications in many domains ranging from web development and competitive programming. Let's discuss certain ways in which this problem can be solved.

Input : test_str = 'Gfg is best' 
Output : {'Gfg': 1, 'is': 1, 'best': 1} 
Input : test_str = 'Gfg Gfg Gfg' 
Output : {'Gfg': 3}'''
from collections import Counter


test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# result = {key:test_str.count(key) for key in test_str.split() }
# print(result)
    # 
# result = Counter(test_str.split()) #Dict subclass for counting hashable items. Sometimes called a bag or multiset. Elements are stored as dictionary keys and their counts are stored as dictionary values.

# print(dict(result))
listString = test_str.split()

freq = {word: listString.count(word) for word in set(listString)}
 
# Printing result
print("The words frequency : " + str(freq))





