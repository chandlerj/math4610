## A review & summary (Sep 20)

**Problem:** Approximate `f'(a)`

Initially, we used the traditional definition from calculus:

*forward difference*: `f'(a) = f(a+h) - f(a) / h`

*backwards difference*: `f'(a) = f(a) - f(a-h) / h`

*central difference*: `f'(a) = f(a+h) - f(a-h) / 2h`

Recall that our `h` value creates unstable results as `h` converges with zero. We needed to determine the smallest value of `h` we can use (the `maceps` value). 

From here, we need to use taylor series to approximate our derivative to abritary precision.

This allows us to form the following relationships:

*forward difference*: `e_abs <= Ch^1`

*backwards difference*: `e_abs <= Ch^1`

*central difference*: `e_abs <= Ch^2`

Recall: `C = 1/2|f''(c)|h`, where `c` is the largest possible s.t. the relationship still holds. That is to say `c` is between `a` & `a + h`

This table shows the error of each `h` as we bring `h -> 0`.
| Table of errors | | | |
|---|---|---|---|
| **h** | **e_abs(h)** | **log(h)**| **log(e_abs(h))**| 
| h_0 | e_abs(h_0) | log(h_0)| log(e_abs(h_0))| 
| h_1 = (h_0)/2 | e_abs(h_1) |log(h_1)| log(e_abs(h_1))|
| h_2 = (h_1)/2 | e_abs(h_2) |log(h_2)| log(e_abs(h_2))|
| h_n = (h_n-1)/2 | e_abs(h_n) |log(h_n)| log(e_abs(h_n))|

Putting this all together:

`e_abs(h) <= Ch^r`

`=> log(e_abs(h)) <= log(C h^r)`

`= log(C) + log(h^r) = log(C) + rlog(h)`

We want to fit this dataset to a linear polynomial. This means we want `y_0 = a + bx_0`. 

*September 22*

## Finally some goddamn code

**Derivative-approx.py**
```
#
# the code in this file will approximate the derivative of a "smooth" function
# using a forward difference
#
# storage
import numpy as np
import matplotlib.pyplot as plt
#
#
# test function for computing derivatives
#
# the derivative
# --------------
#
def f(x):
    fval = x * np.exp(-x)
    return fval
#
# the exact derivative expression
# -------------------------------
#
def df(x):
    dfval = np.exp(-x) - x * np.exp(-x)
    return dfval
#
# the difference quotient for the derivative approximation
# --------------------------------------------------------
#
def dfapp(x, h):
    appval = ( f(x+h) - f(x) ) / h
    return appval
#
# location for the derivative along with an array for increment to use in the
# approximation and an array to store the error for each value tested
# -------------------------------------------------------------------
#
x0 = 1.2
napprox = 50
h = []
error = []
#
# initialize the increment to do the initial approximation
# --------------------------------------------------------
#
hval = 1.0
#
# compute the "exact" derivative
# ------------------------------
#
dfexct = df(x0)
#
# loop over i for generating a list of approximate values
# -------------------------------------------------------
#
for i in range(napprox):
    #
    # compute the difference quotient for the function
    # ------------------------------------------------
    #
    dfappr = dfapp(x0, hval)
    #
    # compute the approximate error between the "exact" value and the approximate
    # value
    # -----
    errval = np.abs(dfappr-dfexct)
    #
    # store the value of the increment and the error for use below
    # ------------------------------------------------------------
    #
    h.append(hval)
    error.append(errval)
    #
    # update the increment by reducing the increment by one half
    # ----------------------------------------------------------
    #
    hval = hval / 2
        #
    # print each of the raw data value for the current index, i, increment,
    # hval,and the current error, error[i]
    # ------------------------------------
    #
    print(i, h[i], error[i])
#
# the rest of the code will bring up a graphical representation of the error
# as a function of the increment, h.
# ----------------------------------
#
plt.plot(h, error)
plt.title("Graph of Error in Derivative Approximation")
plt.xlabel("h (Increment Value)")
plt.ylabel("error (Error in Derivative Approximation)")
plt.show()

```

*   to test the Taylor Series work we will fit the data to our board(?)
    *   we want `h -> e_abs(h) => e_abs(h) <= ch^1`

relationship between `h` and `e_abs(h)`:

| h | e_abs(h) | log(h) | log(e_abs) |  
|---|---|---|---|
|h_0 | e_abs(h_0) | log(h_0) | log(e_abs(h_0)) |
| ... | ... | ... | ... |
| h_m | e_abs(h_m)| log(h_m) | log(e_abs(h_m)) |


These properties allow for the following relationship to form: 


`log(e_abs(h)) = loc(C) + rlog(h)`

`h = 0 => log(e_abs(h_0)) = loc(C) + rlog(h_0)`

`h = 1 => log(e_abs(h_1)) = loc(C) + rlog(h_1)`

`...`

`h = m => log(e_abs(h_m)) = loc(C) + rlog(h_m)`

Consider the generic problem of fitting a data set to a linear polynomial

Given:
| | | | | |
|-|-|-|-|-|
|**x_n**| x_0 | x_1 | ... | x_n |
|**y_m**| y_0 | y_1 | ... | y_m |

`y = a + bx`

the idea is to have: `y_c = a + bx_c`.

we can reconstruct using matrices:

*Matrix A*
| | |
|-|-|
|1 | x_0 |
|1 | x_1 |
|...|...|
|1 | x_n|

*Vector x*
 | |
 |-|
 |a|
 |b|

*Vector y*
 | |
 |-|
 |y_0|
 |y_1|
 |...|
 |y_n|

 We can then compose these to form `Ax = y`.

It is important to note `y` is not a member of the column space of `A` (Denoted `Col(A)`).

But, we can approximate `y` with another vector `p` and project `p` onto `y`, denoted `q`.

 from there `y = q + p`; `q = y - p`.

 We can also deduce that `q` is orthogonal to `p`. It is also true that any vector in `Col(A)` is orthogonal to `q`. We can generate a vector in `Col(A)` using `A*z`. 

 `A*z = z_1*A_1 + z_2*A_2`, where `A_n` is the columns of `A` and `z_n` is the components of vector `z`. So, `(A*z)^T * q = 0 = (A*z)^T(y - p) = (Z^T * A^T)(y-Ax) = Z^T (A^T*y - A^T*x) = 0`. (`^T` being the transpose of a given matrix/vector, and x being an approximation of x).

 therefore, `Ax = y => A^T*Ax = A^T*y`.

 What does `A^T * A` look like? 

 `A^T * A` will be a `2x2` matrix.
 |A^T * A | |
 |-|-|
 |n + 1| sum_(k=0)^(n) (x_k) |
 |sum_(k=0)^(n) (x_k)| sum_(k=0)^(n) (x_k^2) |

  |A^T * y |
 |-|
 |sum_(k=0)^(n) (y_k)|
 |sum_(k=0)^(n) (y_k)|

 **Implementing all this in code**
 ```
 a_11 = n + 1

 a_12 = sum_(k=0)^(n) (x_k)

 a_21 = a_12

 a_22 = sum_(k=0)^(n) (x_k)^2

 b_1 = sum_(k=0)^(n) (y_k)

 b_2 = sum_(k=0)^(n) (x_k)(y_k)

 x_1 = 1/det(A) (a_22 + b_1 - a_12 + b_2)

 x_2 = 1/det(A) (-a_12*b_1 + a_11*b_1)
 ```

**Resulting matricies**

|A | | | |
|-|-|-|-|
|1|log(h_0)|
|1|log(h_1)|
|1|...|
|1|log(h_m)|

|x| | | |
|-|-|-|-|
|log(c)|
|r|

|b | | | |
|-|-|-|-|
|log(e_abs(h_0))|
|log(e_abs(h_1))|
|...|
|log(e_abs(h_m))|


