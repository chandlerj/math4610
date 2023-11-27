import numpy as np


def findLargestEigenvalue(A: np.array, v0: np.array, tol: float, maxIter: int):
    lambda0 = 0
    for _ in range(maxIter):
        v1 = A @ v0 / np.linalg.norm(A @ v0)
        lambda1 = (v1.T @ A @ v1) / (v1.T @ v1) 

        error = abs(lambda1 - lambda0)

        if(error < tol):
            return lambda1
        lambda0 = lambda1
        v0 = v1

def findSmallestEigenvalue(A: np.array, v0: np.array, tol: float, maxIter: int):
    # invert matrix using LU-decomp and then feed A^-1 into findLargestEigenvalue to get smallest Eigenvalue
    AInverse = invertMatrix(A)
    return findLargestEigenvalue(AInverse, v0, tol, maxIter)

def shiftedPowerMethod(A: np.array, v0: np.array, tol: float, maxIter: int):
    #first find largest and smallest eigenvalues, then find midpoint and create matrix shifted to midpoint. From there, find largest eigenvalue of shifted matrix.
    n = len(A)

    l_evalue = findLargestEigenvalue(A, v0, tol, maxIter)
    s_evalue = findSmallestEigenvalue(A, v0, tol, maxIter)

    midpoint = (l_evalue + s_evalue) / 2

    shifted_m = (A - (midpoint * np.identity(n))) * v0
    shifted_l_evalue = findLargestEigenvalue(shifted_m, v0, tol, maxIter)

    return shifted_l_evalue

def findEvalInterval(A: np.array, v0: np.array, tol: float, maxIter: int, numPartitions: int):
    n = len(A)
    l_evalue = findLargestEigenvalue(A, v0, tol, maxIter)
    s_evalue = findSmallestEigenvalue(A, v0, tol, maxIter)
    # print(f'smallest e-val: {s_evalue}, largest e-val: {l_evalue}')
    # create partitions between largest and smallest eigenvalue

    eigenvalues = []
    eigenvalues.append(l_evalue)
    eigenvalues.append(s_evalue)
    partition_size = (l_evalue - 1 - s_evalue) / numPartitions
    for i in range(1, numPartitions + 1):
        shift_val = s_evalue + (i * partition_size)

        shifted_m = (A - (shift_val * np.identity(n))) * v0
        eigenvalues.append(abs(findLargestEigenvalue(shifted_m, v0, tol, maxIter)))
    return eigenvalues
def findTwoLargestEvalues(A: np.array, v0: np.array, tol: float, maxIter: int):
    
    eVec_list = findEvalInterval(A, v0, tol, maxIter, 10) 
    n = len(eVec_list)
    eVec_list.sort()
    return (eVec_list[n-1], eVec_list[n-2])
def invertMatrix(A: np.array):
    n = len(A)
    result = np.copy(A)
    lower, upper = LU_Defactor(A)
    
    b = np.zeros(n)
    for i in range(n):
        for j in range(n):
            if i == upper[j].any():
                b[j] = 1.0
            else:
                b[j] = 0.0
        x = forwardBackelim(lower, b)
        for j in range(n):
            result[j][i] = x[j]
    return result

def createDiagDominantMatrix(size):
    # create a diagonally dominant matrix
    matrix = np.random.rand(size, size)
    for i in range(size):
        diagonalEntry = sum(matrix[i]) + 1
        matrix[i][i] = diagonalEntry
    return matrix

def LU_Defactor(A: np.array):
    n = len(A) # number of rows in square matrix

    lower = np.eye(n, dtype=np.double)
    upper = A.copy()

    for i in range(n):
        factor = upper[i + 1:, i] / upper[i,i]
        lower[i+1:, i] = factor
        upper[i+1:] -= factor[:, np.newaxis] * upper[i]
    return lower, upper #returning both since i calculate both

def forwardBackelim(lower, b):
    n = len(lower)
    x = np.copy(b)

    x[0] = b[0]
    for i in range(1,n):
        total = x[i] 
        for j in range(i):
            total -= lower[i][j] * x[j]
        x[i] = total
    x[n - 1] /= lower[n-1][n - 1]

    for i in range(n-2, -1, -1):
        sum = x[i]
        for j in range(i + 1, n):
            sum -= lower[i][j] * x[j]
        x[i] = sum / lower[i][i]
    
    return x

    
def backSub(A: np.array, y: np.array):
    x = np.zeros(len(y))
    n = len(y)


    
matrix = createDiagDominantMatrix(5)
guess1 = np.array([[1, 1, 1, 1, 1]]).T
matrix2 = np.array([[2.0,1.0], [1.0,2.0]])
guess2 = np.array([[1.0,2.0]]).T
leslie_m = np.array([[0,1,1.5,1.2],[.8,0,0,0],[0,0.5,0,0],[0,0,0.25,0]])
leslie_guess = np.array([[1,1,1,1]]).T
print(findLargestEigenvalue(leslie_m, leslie_guess, 0.001, 100))
print(findLargestEigenvalue(matrix, guess1, 0.001, 100))
print(shiftedPowerMethod(matrix, guess1, 0.001, 100))
print(findTwoLargestEvalues(matrix, guess1, 0.001, 100))
print(findEvalInterval(matrix, guess1, 0.001, 100, 5))

print(findSmallestEigenvalue(matrix2, guess2, 0.0001, 100))
print(findLargestEigenvalue(matrix2, guess2, 0.001, 100))
