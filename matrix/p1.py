'''Adding and Subtracting Matrices in Python
Suppose we have two matrices A and B.
A = [[1,2],[3,4]]
B = [[4,5],[6,7]]

then we get
A+B = [[5,7],[9,11]]
A-B = [[-3,-3],[-3,-3]]'''
import numpy as np

a= np.array([[1,2],[3,4]])
b= np.array([[1,2],[3,4]])

print("first array\n",a)
print("second array\n",b)
result = np.add(a,b)
print("Adding of two matrix---")
print(result)
print("Substracting of two matrix ---")
print(np.subtract(a,b))

print("printing elements of first matrix -----")
for row in a:
    for ele in row:
        print(ele,end=" ")
    print()

print("printing elements of Second matrix -----")
for row in b:
    for ele in row:
        print(ele,end=" ")
    print()

# addition of two matrix 
result = [[0,0],[0,0]]
for i in range(len(a[0])):
    for j in range(len(a)):
        result[i][j] = a[i][j] + b[i][j]
    
print("printing elements of Sum of  matrixs-----")
for row in result:
    for ele in row:
        print(ele,end=" ")
    print()