'''Given two matrices X and Y, the task is to compute the sum of two matrices and then print it in Python. 
Examples: 

Input :
 X= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
Output :
 result= [[10,10,10],
         [10,10,10],
         [10,10,10]]'''

 
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
import numpy as np
# for i in range(len(X)):
#     for j in range(len(Y[0])):
#         result[i][j] = X[i][j] + Y[i][j]

# result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

result = np.array(X) + np.array(Y)
print(result)
