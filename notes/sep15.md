## Taylor Series Approximation

*Theorem*: Suppose `f` has infinitely many derivatives near a point `a`, then the taylor series is given by:

`f'(x) = f(a) + f'(a)(x - a) + 1/2f''(a)(x - a)^2`

In general: `sum(n = 0 -> inf) (f^(n)(a))/(n!) (x - a)^n`
*   remember, f^(n) is the n-th derivative.

Increment notation: `f(a + h) = f(a) + f'(a)(a + h - a) + 1/2f''(a)(a + h - a)^2`

Summation: `sum(n = 0 -> inf) (f^(n)(a) / h) * h^n`

**taylor series error approximation:**

consider: err = `|f'(a) - 1/h (f(a + h) - f(a))|`

err ~= `f'(a) - 1/h[f(a) + (f'(a)/1!)*h + (f''(a)/2!) * h] - f(a)`

which cancels to `|-1/2 f''(a)h - 1/6 f'''(a)* h^2 + ...|`

We can take the taylor series with remainder. For our purposes we could define: `f(a + h) = f(a) + f'(a)h + 1/2f''(c) * h^2`.

*   where `c` is a value between `a` and `a + h`

We can then redefine the error to be:

err ~= `|1/2 h * f''(c)| = 1/2 * h * f''(c)`

*   the last component of the taylor series remainder approximation is the remainder.

*Example*: `f(x) = e^x; a = 1`

*   `f^(0)(x) = e^x` -> `f^(0)(1) = e^1` -> `f^(0)(1) / 0! = e^1`

    `f^(1)(x) = e^x` -> `f^(1)(1) = e^1` -> `f^(1)(1) / 1! = e^1`

    `f^(2)(x) = e^x` -> `f^(2)(1) = e^1` -> `f^(2)(1) / 2! = e^1 / 2!`

    `R_1(x, a) = (f^(3)(c) / 3!) (x - 1)^3`

*   `f(x) = c_0(x - 1)^0 + c_1(x-1)^1 + c_2(x - 1)^2 + R_1`

    `= e^1 + e^1(x - 1) + e^1/2(x - 1)^2 + e^c/3! (x - 1)^3`

This will give us an upper bound for the error for our approximation (`R_1`).

For `f'a ~= (f(a + h) - f(a)) / h`, the error is given by `1/2 h f''(c) <= M * h'`, where `M = 1/2 |f'(c)|`.

*Example*: `f'a = (f(a + h) - f(a)) / h` where `h > 0`.

`err = |f'(a) - (f(a + h) - f(a)) / h|`

`=| f'(0) - 1/h(f(a) - (f(a) + f'(0)(a - (a - h)) + 1/2 f''(a) (a - (a - h))^2 ) |`


