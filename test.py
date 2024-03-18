'''lst = [1,2,3,4,5]
print(lst)

new_list = list(map(str,[i for i in range(10)]))
print(new_list)

y = '-'.join(new_list)
print(y)
print(type(y))

# taking input using map 
# n = input('how maby input do u wanna take :')
a, b,c= map(int,input().split(' '))
'''
# n = 5
# if n%2: #odd 
#     print('hi')
# else:
#     print('hello')

# s = 'Guitor'
# rev = reversed(s)
# lst =list(i for i in range(1,5))
# updated_list = list(map(str,lst))
# print(updated_list)
# print(lst)

# rev_list = reversed(updated_list)
# str1 = '-'.join(updated_list)
# str2 = ','.join(rev_list)
# print(str1,str2)

# names = ['Mukesh', 'Roni', 'Chari']
# ages = [24, 50, 18]

# li = zip(names, ages)
# print(li)
# for i, (name, age) in enumerate(li):
# 	print(i, name, age)
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]

# using zip() to map values
mapped = zip(name, roll_no)

print(set(mapped))
