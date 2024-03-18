'''Transpose a matrix in Single line in Python
Input: [[1,2],[3,4],[5,6]]
Output: [[1,3,5],[2,4,6]]
Explanation: Suppose we are given a matrix
                       [[1, 2],
                        [3, 4],
                        [5, 6]]
Then the transpose of the given matrix will be, 
                       [[1, 3, 5],
                        [2, 4, 6]]
'''

'''m = [[1, 2], [3, 4], [5, 6]]
for row in m:
	print(row)
rez = [[m[j][i] for j in range(len(m)) ] for i in range(len(m[0])) ]

print("-----------\n")
for row in rez:
	print(row)'''

matrix = [(1, 2, 3), (4, 5, 6), 
				(7, 8, 9), (10, 11, 12)]
# for row in matrix:
# 	print(row)
# print("\n")

# print(*matrix)
# print([i for i in zip(*matrix)])
t_matrix = zip(*matrix)

# for row in t_matrix:
# 	print(row)



# stocks = ['GEEKS', 'For', 'geeks']
# prices = [2175, 1127, 2750]

# new_dict = {stocks: prices for stocks,prices in zip(stocks, prices)}
# print(new_dict)

stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
			prices in zip(stocks, prices)}
print(new_dict)

import numpy as np
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
print("\n")
print(np.transpose(matrix))

matrix = np.array(matrix)
print('--------Transpose by array.T')
print(matrix.T)
