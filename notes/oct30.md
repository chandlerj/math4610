*october 30*

## What we need for assignment 5

- Gaus Elimination + Back substitution
- LU-factorization + Forward elimination + Back substitution
- Matrix-vector Product
- L2 Error in a euilidian norm
- testing routine for the functions
- generate a diagionally dominant matrix
- SOFTWARE MANUAL


## Assignment 6: root finding

- Fixed point iteration (?)
- Bisection
- Newton's method
- Secant method
- Hybrid method
    - there are two different implementations of this

# Using the power method for computing the largest Eigen-value of a square matrix

**Def**: An Eigenvector `v in R^n` is a nonzero vector such that for some number `lambda in R`:
$$
A \vec{v} = \lambda \vec{v}
$$ 

The runtime clompexity for the LHS of this equation has runtime complexity O(n^2) and the RHS has complexity O(n).

Suppose we start with some vector `v` and assume `v = alfa_0 * v_0 + alfa_1 * v_1 + ... + alfa_n * a_n`, where `{v_1, ..., v_n}` are the eigenvectors of `A`. Assume `{v_1, ..., v_n}` is a basis for `R^n`.

We can order the eigenvalues S.T

$$
\lambda_1 \geq \lambda_2 \geq \lambda_3 \leq ... \leq \lambda_n
$$

Compute the following

$$
\vec{u}  =A \vec{v}\\
= A(\alpha_1 v_1 + \alpha_2 v_2 + ... + \alpha_n v_n)\\

= A\alpha_1 v_1 +  A\alpha_2 v_2 + ... + A\alpha_n v_n\\

= \lambda\alpha_1 v_1 +  \lambda\alpha_2 v_2 + ... + \lambda\alpha_n v_n\\

w = A(A\vec{v})\\


= \lambda_1^2\alpha_1 v_1 +  \lambda_2^2\alpha_2 v_2 + ... + \lambda_n^n\alpha_n v_n\\

A^k\vec{v} = \lambda_1^k\alpha_1 v_1 +  \lambda_2^k\alpha_2 v_2 + ... + \lambda_k^n\alpha_n v_n\\

= \lambda_1^k(\alpha_1 v_1 + \alpha_i(\frac{\lambda_2}{\lambda_1})^k + ... + \alpha_n(\frac{\lambda_n}{\lambda_1})^k)
$$

## Implementing the method algorithmically

$$
v \neq 0\\
y = Av = \alpha_1 \lambda_1 v_1 + ... + \alpha_n \lambda_n + v_n\\
w = \frac{1}{||y||} * y
$$

input for algo: `A, v0, tolerance, maxIter`

*note*: `v0` cannot be the zero vector
```
# python3
for i in range(maxIter):
    v1 = A * v0
    lambda0 = 0
    lambda1 = rayleigh(A, v1)

    error = abs(lambda1 - lambda0)

    if (error < tol) return lambda1
    lambda0 = 1
    v0 = v1
```

### Rayleigh Quotient

if `v` is an eigenvector of `A` with eigenvalue `lambda` then
$$
\frac{v^t A v}{v^t v} = \lambda
$$

*November 1*

### Power Method

$$
A \in \R^{n * n}
$$

`A` has a dominant eigenvalue (Magnitude)

**Implementation**

**Inputs**: `A`, `v0`, `tol`, `maxIter`

```
import numpy as np

def power_method(A: np.array, v0: np.array, tol: Int, matIter: Int):
    #initialization of params
    error = 10 * tol # guarantees at least 1 iteration
    lambda0 = 0

    #loop tim
    while (error > tol and iter < maxiter):
        y = A * v0
        v1 = 1 / magnitude(y) * y # Rayleigh quotient
        lambda1 = transpose(v1) * A * v1
        error = abs(lambda1 - lambda0)
        lambda0 = lambda1
    return lambda1 # largest eigenvalue
```

This routine will return the largest eigenvalue of a matrix. It is very inefficient and has plenty of room for optimizations.

**Modified power method**

This implementation will have a shorter computation runtime. This is because we only do one matrix vector operation versus the origanal implementation which does two matrix vector operations.

**Inputs**: `A`, `v0`, `tol`, `maxIter`
```
def imp_power_method(A, v0, tol, maxIter):
    #initialization of parameters
    v0 = 1/magnitude(v0) * v0
    y = A * v0
    lambda0 = transpose(v0) * y
    error = 10 * tol
    iter = 0

    #da loop
    while error > tol and iter < maxIter:
        v1 = 1 / magnitude(y) * y
        y = A * v1
        lambda1 = transpose(v1) * y
        error = abs(lambda1 - lambda0)
        iter += 1
        lambda0 = lambda1
    return lambda1 # largest eigenvalue
```

What if we want more than one eigenvalue? We can modify this algorithm to provide the smallest eigenvalue (in magnitude)

$$
|\lambda_1| \geq |\lambda_2| \geq ... \geq |\lambda_{n-1}| \geq |\lambda_n| > 0
$$

**Theorem**: if `lambda` is an eigenvalue of `A in R^{n * n}`, then `1 / lambda` is an eigenvalue of `A^{-1}.

*Hand-wave* **Proof**:

Assume
$$
Av = \lambda v\\
$$
then,
$$
v = \lambda A^{-1} v\\
A^{-1} v = \frac{1}{\lambda} v
$$