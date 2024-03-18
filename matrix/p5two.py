from itertools import chain
import time
import numpy as np

def Transpose2(M):
    n = len(M[0])
    L = list(chain(*M)) 
    return [L[i::n] for i in range(n)]

start= time.time_ns()
matrix = np.array([[1,2,3],[4,5,6]])
end = time.time_ns()
print(Transpose2(matrix))
print("Time taken : "+str(end-start)+"ns")

