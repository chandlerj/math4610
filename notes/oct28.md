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
# python3
for _ in range(max_iter):
    x1 = x0 - (f(x0) / f'(x0))
    err = abs(x1 - x0)
    x0 = x1 
```

*October 25*

**Fixed Point iteration**

Consider the function:
$$
g(x) = x + m f(x)\\ m = 0.1,0.2,0.3,...,
$$

We need to find non trivial values of `m` to find meaningful roots.

**Newton's Method Cont.**

- Newton's Method's primary disadvantage is that it requires a lot of additional computations and parameters.

- Newton's method is referred to as a *quadratic* convergence. Whereas methods like Fixed point and Bisection are considered *linear* convergence.

**Tha Secant Method**

This method is similar to Newton's Method. Recall Newton's method:
$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
$$

We modify this function to the following:

$$
x_{k+2} = x_{k+1} - \frac{f(x_{k+1})}{\frac{f(x_{k+1} - f(x_k))}{x_{k+1} - x_k}}\\
= x_{k+2} = x_{k+1} - \frac{f(x_{k+1})* (x_{k+1} - x_k) }{f(x_{k+1} - f(x_k))}\\
$$


**Inputs**: `f(x), x_1, x_0, tol`

We need `f` to be:

- `f'(x) =/= 0`
- `f in c^2[a,b]`
- `x_0` and `x_1` must be sufficiently close to the root

Recap - We have discussed the following methods:

- fixed point iteration: `rate: 1`, `Convergence: linear`
- Bisection: Same properities as fixed point
- Newton's Method: `Convergence: quadratic`
- Secant Method: `rate: 1.65`

**Finding the rate of convergence**

$$
x_0, e = |x_0 - x^*|\\
x_1, e = |x_1 - x^*|\\
...\\
x_n, e = |x_n - x^*|\\
|x_{k+1} - x^*| \leq C|x_k - x^*|^k\\
e_{kn} \leq Ce^n_k\\
\log(e_{kn}) = \log(C) + r\log(e_k)
$$

The result of these equations will provide the rate of convergence for a given root finding method.

When trying to find roots, it may be beneficial to bound to a region of the function, use bisection to narrow in to the root, and then use newton's method to get a closer approximation

**Hybrid method**

- bracket a root between `[a_0, b_0], f(a_0) * f(b_0) < 0`
    - satisfying these conditions ensures we can use the bisection method
- take some number of steps of bisection to reduce this method. Reduce by `10^-1`.
- try Newton's method at this point because the convergance is faster
    - If Newton's method fails, return to bisection and continue reducing
    - else, continue reducing with Newton's method.

to determine our bisection reduction, we can use the following method:
$$
|b_{k+m} - a_{k+m}| \leq (\frac{1}{2})^2 |b_k - a_k|\\
m \gt 3.x \rightarrow m = 4
$$


*October 27*

If we do not know where a root is, we will need to bracket a root. One strategy at this point is to use a bisection criteria for a root.

**Def**: Hybrid Method - combining bisection and higher order method. Some examples of higher order methods include:

- Newton's Method
- Secant Method

**Implementing Hybrid Method**

**Inputs**: `f, f', [a_0, b_0], tolerance, maxIterations`

```
#include <errno.h>        /* errno */

//initialize variables
fa = f(a)
fb = f(b)

if (fa * fb >= 0){
    perror("invalid range for a,b")
}
error = 1.0 * tolerance;
iter = 0;

while(error > tol && iter < maxIterations){
    iter++;
    x_0 = 0.5 * (a + b);
    x_1 = x_0 - f(x_0)/f'(x_0);

    if( abs(x_1 - x_0) > 0.5 * (b - a)){
        c = x_0;
        fc = f(c);
        for(int i < 0; i < 4; i++){ //do 4 iterations of bisection to reduce order of magnitude of problem by 1
            if(fa * fc < 0){
                b = c;
                fb = fc;
            }
            else{
                a = c;
                fa = c;
            }
            c = 0.5 * (a + b);
        }
        x_0 = c;
    }
    else{
        while(error > tolerance){ //do newtons method
            x_1 = x_0 - f(x_0)/f'(x_0);
            error = abs(x_1 - x_0);
        }
    }
}
```
**Expanding the horizons (parallelism)**


We can do this process over the whole number line and subdivide the line into `h` intervals. when the value of `a + mh` and `a + (m + 1)h` where `m` is some integer changes from >0 to <0 or vice versa, there is a root in that interval. In addition, you could also take a parallel approach where every time a root is found, a new thread determines the root over that interval while the main thread continues scanning for potential roots.