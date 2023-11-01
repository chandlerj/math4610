import numpy as np

def multiplyMatrixByVector(A, b):
    row_size = len(A[0])

    n = len(b)
    total = np.zeros(n)

    for i in range(n): # for every element in the vector b
        
        for j in range(row_size): # for every component in row i of the matrix A
            print(f"{b[i] * A[i][j]}") 
            total[i] += b[i] * A[i][j]
    return total