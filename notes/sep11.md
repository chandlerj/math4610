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