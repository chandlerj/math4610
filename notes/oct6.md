<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>


## Creating a shared library
Below is an example of the terminal commands you may use to create a `C` library

```
% ls
smacups.c   dmaceps.c

% gcc -c -c smaceps.c
% gcc -c -c dmaceps.c

% ls
smacups.c   dmaceps.c   smacups.o   dmaceps.o

% ar crv mylib.a *.o

% ranlib mylib.a //alias for ar

% gcc -o test test.c mylib.a
```

## Expectations for software written in this class

*   Every piece of code needs to be documented
    *  A markdown file has been provided that needs to be filled with the following information for every function, method, etc:
        *  Author
        *  Date
        *  Description of functionality
        *  Usage Example
    *  documentation should contain a table of contents


## Gausian Elimination
`gaus.c`
```
float[][] gaus_elim(float[][] a, float[] b){
    
    int sum;

    for(int k = 0; k < (n-1); k++)
    {
        for(int i = k + 1; i < n; i++)
        {
            //multiplier for reduction on the i-th row
            double factor = a[i][k] / a[k][k];

            for(int j = k + 1; j < n; j++)
            {
                a[i][j] = a[i][j] - (factor * a[k][j]);
            }
            b[i] = b[i] - (factor * b[k]);
        }
    }
    return a, b; //bad syntax; need to return as an array of arrays
}

float[] back_sub(float[][] a, float[] b){
    float[] x; //need to allocate this array

    //back substitution routine
    x[n - 1] = b[n - 1] / a[n - 1][n - 1];
    for(int i = n - 2; i >= 0; i--){
        sum = 0.0;
        for(int j = i+ 1; j < n; j++)
        {
            sum = a[i][j] * x[j];
        }
        x[i] = (b[i] - sum) / a[i][i];
    }

    return x;
}
```


Suppose we need to solve:

$$ Ax^{(k)} = b^{(k)} $$

We want to consider `LU-factorization`:

$$A = L * U$$

where `L` is a lower triangular maxtrix and `U` is an upper triangular matrix. If `A = L * U`, then

$$Ax = b \rightarrow L * Ux = b\\ \rightarrow Ly = b \rightarrow Ux = y$$

*Example:*

$$A = 
\begin{pmatrix}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}\\
\end{pmatrix}
= \quad
\begin{pmatrix}
l_{11} & 0 & 0\\
l_{21} & l_{22} & 0\\
l_{31} & l_{32} & l_{33}\\
\end{pmatrix}
*
\begin{pmatrix}
u_{11} & u_{12} & u_{13}\\
0 & a_{22} & u_{23}\\
0 & 0 & u_{33}\\
\end{pmatrix}
$$
hence,
$$
\\a_{11} = l_{11} u_{11}
$$

**finding the components of upper & lower matrix**

$$u_{11} = a_{11}\\
u_{12} = a_{12}\\
u_{13} = a_{13}\\
l_{21}u_{11} + 0 + 0 = a_{21}\\
l_{21} = \frac{a_{21}}{u_{11}}\\
l_{31} = \frac{a_{31}}{u_{11}}\\
l_{21} u_{12} + u_{22} = a_{22} \rightarrow u_{22} = a_{22} - l_{21}u_{12}\\
l_{31} u_{13} + u_{21} = a_{23} \rightarrow u_{32} = a_{23} - l_{32}u_{13}$$



*October 9*
## LU Factoriztion continued


$$A = 
\begin{pmatrix}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}\\
\end{pmatrix}
$$

Perform the following operations to reduce the matrix to an upper triangular form:
$$l_{21} = -\frac{a_{21}}{a_{11}}, \quad l_{31} = -\frac{a_{31}}{a_{11}} $$


$$ 
\begin{pmatrix}
1 & 0 & 0\\
-\frac{a_{21}}{a_{11}} & 1 & 0\\
-\frac{a_{31}}{a_{11}} & 0 & 1\\
\end{pmatrix}

*

\begin{pmatrix}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}\\
\end{pmatrix}

=

\begin{pmatrix}
a_{11} & a_{12} & a_{13}\\
0 & (a_{22} - \frac{a_{21}}{a_{11}} a_{12}) & (a_{23} - \frac{a_{22}}{a_{11}} a_{13})\\
a_{31} & (a_{32} - \frac{a_{31}}{a_{11}} a_{13}) & (a_{33} - \frac{a_{32}}{a_{11}} a_{13})\\
\end{pmatrix}
$$

We can program in the exact computations we want to reduce this matrix. This reduces program complexity.

$$A^1 \in \R^{n*n}, \\
M^0 = \begin{pmatrix}
1 & 0 & 0 & ... & 0\\
-\frac{a_{21}}{a_{11}} & 1 & 0 & ... & 0\\
-\frac{a_{31}}{a_{11}} & 0 & 1 & ... & 0\\
-\frac{a_{41}}{a_{11}} & 0 & 0 & ... & 0\\
...\\\
-\frac{a_{n1}}{a_{11}} & 0 & 0 & ... & 1\\

\end{pmatrix}
$$

We will iterate through each column of `A` and construct an `M` matrix to eliminate that column following the pattern outlined above. Doing this iteratively will result in an upper triangular matrix `U`.


We can derive the following relationship from this procedure.
$$
MA = U\\ A = M^{-1} U = LU
$$

*October 11*

## Gaus Elimination Continued

**Theorem**: Suppose that `A` is an element of the `R^(n x m)` set and is diagonally dominant then guassian elimination of `A` produces no zero pivot elements.

**Definition:** `A` is diagonally dominant if for each `i = 1, 2, ..., n`,
then

$$
|a_{i,i}| \geq \sum_{j=1}^{n} |a_{i,j}|
$$

with strict magnitude for at least row 2. (?)

**Test our GE w/ Back substitution**
*   Generate a diagonally dominant matrix.
    *   set `a_{i,j}` to be a random number `[0,1]`
    *   set `a_{i,i} = n + 1`
    *   this gives you matrix `A`
*   set 
$$ A = 
\begin{pmatrix}
1\\1\\1\\...\\1\\
\end{pmatrix}
$$

* compute `b = Ay`
* solve `Ax = b`
* Compute an `L2-Distance(x,y)`

*October 13*

## LU-Factorization

we need to solve `A = LU`. To find this solution we need to compute `Ly = b` and `Ux = y`. Solving `Ux = y` will implement back substition

## Forward Elimination
This will allow us to 
```
y[0] = b[0]
for i in range(1, n):
    sum = 0.0
    for j in range(i - 1):
        sum = sum + a[i][j] * y[j]
    y[i] = b[i] - sum
```

**How to test the code**
*   Generate a diagonally dominant matrix `A`
    *   randomly fill a matrix with values [0,1], and then multiply the diagonal values by a large constant to make the matrix diagonally dominant.
*   perform matrix multiplication of `A[1,1,1,...,1]^T = b`, `y = [1,1,1,1,...,1]^T`
*   solve `Ax = b`
*   error = `||x - y||`

# Root Finding (New topic)

problem description: Find `X in Reals` such that `f(x) = 0`.

If `g(x)` is a function and we want to find `x` such that `g(x)` is external, then we find `x in reals` s.t. `g'(x) = 0`.

