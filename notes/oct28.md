## Matrix Multiplication into a vector
*October 23*

A matrix multiplication algorithm can be written in the following way:

**Input:** `A in R^(nxn), x in R^n`

**Output:** `y = Ax in R^n`

```
//matrix_mult.c

double y[];

double* Matrix_mult(double** A, double* x){
    for(int i = 0; i < n; i++){

        double sum = 0.0;
        for(int j = 0; j < n; j++){
            sum = sum + a[i][j] * x[j];

        }
        y[i] = sum;
    }
    return y;
}
```

You might want to create a routine that performs the dot product of a vector. In our code above, the dot product is computed in the second `for` loop.

```
//dot_prod.c

double dot_prod(double* v_1, double* v_2){
    sum = 0.0;
    for(int i = 0; i < n; i++){
        sum += v_1[i] * v_2[i];
    }
}
```

### Alternative ordering of `for` loops

Given the matrix

$$
Ax = x_1
\begin{pmatrix}
a_{11}\\
a_{21}\\
...\\
a_{n1}\\

\end{pmatrix}

+ x_2
\begin{pmatrix}
a_{12}\\
a_{22}\\
...\\
a_{n2}\\
\end{pmatrix}
+
... +
x_n
\begin{pmatrix}
a_{1n}\\
a_{2n}\\
...\\
a_{nn}\\

\end{pmatrix}
$$

We can write the following code to multiply this matrix

```
for(int i = 0; i < n; i++){

    sum = 0.0;
    for(int j = 0; j < n; j++){
        sum += a[i][j] * x[j];
    }
    y[i] = sum;
}
```

lets flip the `for` loops

```
for(int j = 0; j < n; j++){
    for(int i = 0; i < n; i++){
        y[i] = y[i] + a[i][j] * x[i];
    }
}
```
This gives a faster execution since we are accessing elements that are closer to one another. This means the values will already be stored in the cache when the number is retrived.

## Root Finding Continued

**Recap**: We want to find `x` such that `f(x) = 0`

We have explored:
*   Fixed point iteration
    *   find `g(x)` related to `f(x)` such that if `x = g(x) => x_{k+1} = g(x_k), k = 0,1,2,...,n`

    *   We can then assert `|g(x_*)| < 1`
*   Bisection method
    *   Based on the itermediate value theorem.
    *   assumes `f` is continuous on an interval `[a,b]`
        *   additionally, `f(a)*f(b) < 0`

### Newton's method
*   uses a tangent line approximation
*   `f(x) = f(x_0) + f'(x_0)(x - x_0) + h.o.t.`
*   `y(x) = f(x_0) + f'(x_0)(x - x_0)`
*   `y(x_1) = f(x_0) + f'(x_0)(x - x_0) = 0 => x_1 = x_0 - f(x_0) / f'(x_1)`
*   The assertsions above allow for the algorithm
    * `x_{k+1} = x_k - f(x_{k+1})/f'(x_0)`

**Restrictions**
*   `f` must be twice continuously differentiable
*   `f'(x_k) =/= 0`
*   `x_0` must be close to the root in question.

**Code for Newton's Method**

**input:** `f, f', x_0, max_iter`

```
for _ in range(max_iter):
    x1 = x0 - (f(x0) / f'(x0))
    err = abs(x1 - x0)
    x0 = x1 
```

