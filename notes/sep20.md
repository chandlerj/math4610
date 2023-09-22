## A review & summary

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