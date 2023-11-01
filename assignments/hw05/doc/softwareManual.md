# Linear Equation solver software manaul


# Table of Contents
1. [backward substituion](#backsub)
2. [forward elimination](#forward-elimination)
3. [diagonally dominant matrix](#diagonally-dominant-matrix)
4. [Guassian Elimination](#guassian-elimination)
5. [LU-Decomposition](#lu-defactorization)
6. [matrix-vector product](#matrix-vector-multiplication)
7. [Test suite](#test-routine)

## requirements
This program requires the user have `python3` and `numpy` installed on their system. Below is a brief explanation on how to acquire these tools in a `Fedora` linux environment. These instructions can be adapted to any linux distro or MacOS (For MacOS, you will want to use the `brew` package manager).

```
#install python3 and pip package manager for python
sudo dnf install python pip

#install numpy module for python
pip install numpy
```


## backSub
**Routine Name:**           backSub

**Author:** Chandler Justice

**Language:** `Python3`; this code runs in the Python interpreter, and can be included in your software by using `import backsub` 


**Description/Purpose:** This routine will perform back substitution on a system of linear equations to find the resulting matrix `x`

**Input:**
- `A`: A `numpy` array representing a matrix
- `y`: A `numpy` array representing a vector

**Output:** This routine will return a `numpy.array`, `x`, that represents the solutions to `y` given the linear system of equations `A`.

**Usage/Example:**
an example using Back substitution to solve a system of equations reduced by Guassian elimination
```
[A, y0, b] = diagMatrix.createDiagDominantMatrix(10)

[guas_elim , y1] = gausElim.Gaus_elim(A, b)
final_result = backsub.backSub(guas_elim, y1)
```



**Implementation/Code:** The following is the code for back substition

```
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
```

**Last Modified:** Nov/2023

## Forward Elimination
**Routine Name:**           forwardElim

**Author:** Chandler Justice

**Language:** `Python3`; this code runs in the Python interpreter, and can be included in your software by using `import forwardElim` 


**Description/Purpose:** This routine will perform forward elimination on a system of linear equations to find the resulting vector `y`

**Input:**
- `A`: A `numpy` array representing a matrix
- `b`: A `numpy` array representing a vector

**Output:** This routine will return a `numpy.array`, `y`, that represents the solutions to `b` given the linear system of equations `A`.

**Usage/Example:**
An example using forward elimination as a part of the process of finding the solution to a set of linear equations using LU-decomposition
```
    [A_lu, y0_lu, b_lu] = diagMatrix.createDiagDominantMatrix(10)

    [lower_m , upper_m] = LUDefactor.LU_Defactor(A_lu)

    z_lu = matrixVector.multiplyMatrixByVector(lower_m, b_lu)
    
    z1_lu = forwardElim.forward_elim(lower_m, z_lu)

    x_lu = backsub.backSub(upper_m, z1_lu)
```



**Implementation/Code:** The following is the code for forward elimination

```
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
```

**Last Modified:** Nov/2023

## Diagonally Dominant Matrix
**Routine Name:**           diagMatrix

**Author:** Chandler Justice

**Language:** `Python3`; this code runs in the Python interpreter, and can be included in your software by using `import diagMatrix` 


**Description/Purpose:** This routine will generate a diagonally dominant square matrix.

**Input:**
- `size`: the dimensions of the `size x size` matrix

**Output:**
- `matrix`: the resulting matrix
- `y`: a vector of length `size` that is filled with 1s
- `b`: the RHS of the system of generated equations

**Usage/Example:**
An example using a diagonally dominant matrix as a part of the process of finding the solution to a set of linear equations using LU-decomposition
```
    [A_lu, y0_lu, b_lu] = diagMatrix.createDiagDominantMatrix(10)

    [lower_m , upper_m] = LUDefactor.LU_Defactor(A_lu)

    z_lu = matrixVector.multiplyMatrixByVector(lower_m, b_lu)
    
    z1_lu = forwardElim.forward_elim(lower_m, z_lu)

    x_lu = backsub.backSub(upper_m, z1_lu)
```



**Implementation/Code:** The following is the code for forward elimination

```
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
```

**Last Modified:** Nov/2023


## Guassian Elimination
**Routine Name:**          guasElim 

**Author:** Chandler Justice

**Language:** `Python3`; this code runs in the Python interpreter, and can be included in your software by using `import guasElim` 


**Description/Purpose:** this routine will perform guassian elimination to find the solution to a set of linear equations

**Input:**
- `A`: the matrix of linear equations
- `b`: the RHS of the given equations 

**Output:**
- `A`: the resulting matrix of linear equations
- `b`: the resulting RHS of the given equations 


**Usage/Example:**
Using Guassian elimination to solve a linear system of equations.
```
    [A, y0, b] = diagMatrix.createDiagDominantMatrix(10)

    [guas_elim , y1] = gausElim.Gaus_elim(A, b)
    final_result = backsub.backSub(guas_elim, y1)

    error = np.zeros(10)
    for i in range(10):
        error[i] = abs(final_result[i] - y0[i])
    
    print(f'the error of the GE function is represented by this vector:\n{error}')
```



**Implementation/Code:** 

```
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
```

**Last Modified:** Nov/2023



## LU-Defactorization
**Routine Name:**          LUDefactor 

**Author:** Chandler Justice

**Language:** `Python3`; this code runs in the Python interpreter, and can be included in your software by using `import LUDefactor` 


**Description/Purpose:** this routine will decompose a matrix `A` into an upper `U` and lower `L` matricies

**Input:**
- `A`: the matrix of linear equations

**Output:**
- `lower`: the lower triangular matrix
- `upper`: the upper triangular matrix


**Usage/Example:**
Using LU-Defactorization to solve a linear system of equations.
```
    [A_lu, y0_lu, b_lu] = diagMatrix.createDiagDominantMatrix(10)

    [lower_m , upper_m] = LUDefactor.LU_Defactor(A_lu)

    z_lu = matrixVector.multiplyMatrixByVector(lower_m, b_lu)
    
    z1_lu = forwardElim.forward_elim(lower_m, z_lu)

    x_lu = backsub.backSub(upper_m, z1_lu)

    error_lu = np.zeros(10)
    for i in range(10):
        error_lu[i] = abs(x_lu[i] - y0_lu[i]) 
    print(f'the error of the LU-factorization function is represented by this vector:\n {error_lu}')
```



**Implementation/Code:** 

```
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
```

**Last Modified:** Nov/2023



## matrix-vector multiplication
**Routine Name:**         matrixVector 

**Author:** Chandler Justice

**Language:** `Python3`; this code runs in the Python interpreter, and can be included in your software by using `import matrixVector` 


**Description/Purpose:** this routine will multiply a matrix `A`, by a vector `b`, and return a new matrix which the product of `A` and `b`. 

**Input:**
- `A`: A matrix 
- `b`: A vector
**Output:**
- A vector that is the resulting product of `A * b`

**Usage/Example:**
I have used this module in several other examples. Here is the matrix multiplication being used as a part of LU-defactorization
```
    [A_lu, y0_lu, b_lu] = diagMatrix.createDiagDominantMatrix(10)

    [lower_m , upper_m] = LUDefactor.LU_Defactor(A_lu)

    z_lu = matrixVector.multiplyMatrixByVector(lower_m, b_lu)
    
    z1_lu = forwardElim.forward_elim(lower_m, z_lu)

    x_lu = backsub.backSub(upper_m, z1_lu)

    error_lu = np.zeros(10)
    for i in range(10):
        error_lu[i] = abs(x_lu[i] - y0_lu[i]) 
    print(f'the error of the LU-factorization function is represented by this vector:\n {error_lu}')
```



**Implementation/Code:** 

```
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
```

**Last Modified:** Nov/2023

## Test routine
**Routine Name:**        test 

**Author:** Chandler Justice

**Language:** `Python3`; This program can be run using
```
python test.py
``` 


**Description/Purpose:** This program will test all of the previous models by using them to perform Gaussian Elimination and LU-defactorization on a randomly generated 10x10 matrix.

**Input:** This program accepts no arguments

**Output:**
This program does not return any data but does print the results of the test to the screen

**Usage/Example:**
```
chandler@merci math4610 % /usr/local/bin/python3 /Users/chandler/Documents/math4610/assignments/hw05/test.py
the error of the GE function is represented by this vector:
[0.00000000e+00 0.00000000e+00 7.77156117e-16 2.22044605e-16
 4.44089210e-16 2.22044605e-16 2.22044605e-16 3.33066907e-16
 0.00000000e+00 3.33066907e-16]
the error of the LU-factorization function is represented by this vector:
 [0.17806395 0.06557486 0.07052701 0.14313163 0.17230644 0.08931148
 0.39011558 0.4787903  0.63989401 0.76964689]
```



**Implementation/Code:** 

```
import gausElim, backsub, matrixVector,LUDefactor, forwardElim, diagMatrix
import numpy as np
def main():
    #Testing Gaus elim
    [A, y0, b] = diagMatrix.createDiagDominantMatrix(10)

    [guas_elim , y1] = gausElim.Gaus_elim(A, b)
    final_result = backsub.backSub(guas_elim, y1)

    error = np.zeros(10)
    for i in range(10):
        error[i] = abs(final_result[i] - y0[i])
    
    print(f'the error of the GE function is represented by this vector:\n{error}')

    # testing LU Defactorization
    [A_lu, y0_lu, b_lu] = diagMatrix.createDiagDominantMatrix(10)

    [lower_m , upper_m] = LUDefactor.LU_Defactor(A_lu)

    z_lu = matrixVector.multiplyMatrixByVector(lower_m, b_lu)
    
    z1_lu = forwardElim.forward_elim(lower_m, z_lu)

    x_lu = backsub.backSub(upper_m, z1_lu)

    error_lu = np.zeros(10)
    for i in range(10):
        error_lu[i] = abs(x_lu[i] - y0_lu[i]) 
    print(f'the error of the LU-factorization function is represented by this vector:\n {error_lu}')






main()
```

**Last Modified:** Nov/2023

