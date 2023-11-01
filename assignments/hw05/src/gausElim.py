
# import numpy to grab their matrix objects
import numpy as np

def Gaus_elim(A: np.matrix, b: np.array):
    n = len(b)
    
    for k in range(n):
        for i in range(k + 1, n):
            if(i != k):
                factor = A[i][k] / A[k][k]
                for j in range(k + 1, n):
                    # print(A[i][k])
                    A[i][j] = A[i][j] - factor * A[k][j]
                b[i] = b[i] - factor * b[k]
    return A, b