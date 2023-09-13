## Notations and definitions

*Def*: Suppose `x` is real number, and `y` is another real number we will use to approximate `x`. Then the absolute error in approximating `x` with `y` is `e_(abs) (x,y) = |x - y|`.
*   the relative error is defined by `e_(rel) (x,y) = (|x - y|)/(|x|)`

*Def*: A norm of a vector space, `||v||`, is a function from `R^n`such that
*   `||v|| >= 0` for all vectors in the real space
*   `||v|| == 0` iff `v=0`
    *   these conditions are referred to as positive definitiveness
*   `||e v|| = |e| ||v||` for all `e` and `v` in the reals
*   `||x + y|| < ||x|| + ||y||`, for all real vectors

*Def*: the length of a vector in a quiler norm is defined to be `||v||` for all `v` in real vector space.
*   all normals on finite dimensional vectors are equivilent. then constraints constraints `alf, beta > 0` s.t. `alf||v||_p <= ||v||_q <= beta||v||_p`

*Def*: Suppose `u, v` are real vectors, then the difference between `u` and `v` is `||u-v||`. The absolute error in using a vector `u` to approximate a vector `v` is given by `e_abs = d(v, u) = ||u - v||`. The relative error is given by `e_rel = r(v, u) = (||u - v||)/||v||`

**Table of errors**
|exact | approx. | | |
|---|---|---|---|
| u | v | e_abs | e_rel |
| 1 | 0.99 | 0.01 | 0.01|
| 1 | 1.01 | 0.01 | 0.01 |
| -1.5 | -1.2 | 0.3 | 0.2 |
| 100 | 99.9 | 0.1 | 0.0001|
| 100 | 99 |  1 | 0.01

**looking at `u ~= 0` -> `v ~= 0`**
*   we will consider the absolute error
*   let `u = 1/100, v=1/1000`

|exact | approx. | | |
|---|---|---|---|
| u | v | e_abs | e_rel |
1/100 | 1/1000 | abs((1000-100) / 10^5) | abs(((1000-100) / 10^5)/10^(-2)) |

*Example*: Suppose we want solutions of a linear system of the form `Ax = b`, where `A` is a real matrix, `x,b` are real vectors. Assume that we have an approximation of `x`, say `y` which is a real vector.

We need a measure of the distance between vectors in `R^n`.

`e_abs = ||x - y||`, `e_rel = ||x - y|| / ||x||`.

We can define the residual vector for our system: `r(x) = b - Ax`. if `x` is the solution, then `r(x) = 0`. We can measure the difference using `r(y) = b - Ay =/= 0`. We can measure how close `y` is to a solutuion using the residual.

Even if `r(y) ~= 0`, that doees not imply `||x - y|| = 0`.

*Example*: `||v||_1 = |v_1| + |v_2| + ... + |v_n|`

*   `||v||_inf = max(1 <= i <= n) |v_i|`
*   P-norm: `||v||_p = ((sum_(i=1)^(n) |v_i|^p) * 1/p)`


## time 2 write code
*September 13*

**Objective**: Evaluate `f'(a)` for a function `f(x)` and evaluate at point `a`. We also need to decide how big/small the `h` we choose can be. 
*   will implement the approximation of a limit: `f'(x) = (f(x + h) - f(x)) / h`

*   if we choose an `h` too small, the computer will not have enough precision to determine the difference between `x + h` & `h`. essentially, the computer will resolve `x + h == x`

*   we can find our `e_vel` with the funciton `|((1 + h) - 1) / 1|
`


**test_maceps.c**
```
#include <stdio.h>
#include <math.h>

int main(){
    //float gives about 8 digits of precision. use double for double precision
    float one, appone, h; 
    one = 1.0;
    h = 1.0;
    appone = one + h;
    error = fabs(appone - one);
    while(error > 0.0){
        h = h / 2.0;
        appone = one + h;
        error = fabs(appone-one);
        printf("error = %g  h = %g\n", error, h);
    }
}
```

This program will give us the smallest possible value, the maceps, that the computer be able to interpret as a change in value if the macep is operated on another value.

## Homework 2

*   write some code with the following funcitonality:
    *   maceps - single precision version
    *   maceps - double precision
        *   we need to put these in seperate files/function to avoid decision branching
    *   2-norm of a vector
    *   1-norm of a vector
    *   infinity-norm (aka, soup/max norm) of a vector
    *   2-norm distance between two vectors
    *   1-norm distance between two vectors
    *   infinity-norm between two vectors

**2-norm.py**
```
import numpy as np

def 2norm(vector: list):
    sum = 0.0
    n = len(vector)
    for i in range(n):
        sum = sum + (vector[i] * vector[i])
    sum = np.sqrt(sum)
    return sum
```