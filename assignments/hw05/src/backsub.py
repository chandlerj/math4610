import numpy as np

def backSub(A: np.array, y: np.array):
    x = np.zeros(len(y))
    n = len(y)


    x[n - 1] = y[n-1] / A[n-1][n - 1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += A[i][j] * x[j]
        x[i] = (y[i] - sum) / A[i][i]
    
    return x
