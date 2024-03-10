'''Python program to multiply two matrices'''
# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

 
# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1],]

# multiply  
row =len(B[0])
column = len(A)

result = [[0 for j in range(row)] for i in range(column)]
print(result)
if (len(A[0])) == len(B):
    # print('Okay')
    for i in range(len(A)) : #(0,2)
        for j in range(len(B[0])):#(0,3)
            x =0
            y =0
            result[i][j] = A[i][x] * B[y][j] + A[i][x+1] * B[y+1][j] + A[i][x+2] * B[y+2][j]
            # print(A[i][x],B[y][j],A[i][x+1],B[y+1][j],A[i][x+2],B[y+2][j])
            # print(result[i][j], end =" ")
        # print()

else:
    print("MUltiplication not possible..")


for i in range(len(A)) : #(0,2)
    for j in range(len(B[0])):#(0,3)
        print(result[i][j],end=" ")
    print()
