import numpy as np
import matrixVector

def createDiagDominantMatrix(size):
    # create a diagonally dominant matrix
    matrix = np.random.rand(size, size)
    for i in range(size):
        diagonalEntry = sum(matrix[i]) + 1
        matrix[i][i] = diagonalEntry
    
    # create a vector of 1s
    y = np.full(size, 1)

    # compute product of Ay
    b = matrixVector.multiplyMatrixByVector(matrix, y)
    return matrix, y, b