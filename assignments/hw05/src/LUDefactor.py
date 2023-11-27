import numpy as np

def LU_Defactor(A: np.array):
    n = len(A) # number of rows in square matrix

    lower = np.zeros((n, n))
    upper = np.zeros((n, n))

    for i in range(n):

        for k in range(i, n): # need upper triangular matrix to get lower triangular matrix
            total = 0
            for j in range(i):
                total += (lower[i][j] * upper[j][k])
            
            upper[i][k] = A[i][k] - total
        
        for k in range(i, n):
            if i == k:
                lower[i][i] = 1
            else:
                total = 0
                for j in range(i):
                    total += (lower[k][j] * upper[j][i])
                lower[k][i] = int((A[k][i] - total) / upper[i][i])
    return lower, upper #returning both since i calculate both
