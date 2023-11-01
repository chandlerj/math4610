import numpy as np

def forward_elim(A, b):
    n = len(A)
    y = np.zeros(n)

    y[0] = b[0]
    for i in range(1,n):
        total = 0.0
        for j in range(i):
            total += A[i][j] * y[j]
        y[i] = b[i] - total
    return y