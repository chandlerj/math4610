**GPUs**
*   can come in two forms: Video card & scientific
    *   the distinction is that scientific GPUs have ECC (error correcting memory)
    
**evaluate a derivative of a function at a point**
*   A function can be represented in many forms. A table of inputs/outputs, a graph, or a function definition
    *   `f(x) = e^(-x^2)` -> `f'(x) = -2xe^(-x^2)`
    *   `f'(1) = -2e^-1`. The issue with computing this is that `e` is an irrational number, this means you need `inf` digits to exactly represent it
*   In general, any irrational number cannot be exactly represented on a computer. An infinitely long number will not fit in finite memory.
*   Computing derivatives:
    *   suppose `f(x)` is a function definited on an open interval `I`. Then if `a in I` and `lim(x -> a) (f(x) - f(a))/(x - a)` exists, then we say `f(x)` is differentiable at `x - a`. if `f` is differentiable at all points in `I`, we say `f` is differentiable on `I`. The value of the limit is the deriviative of `f` at `a`.
    *   We can use alternative form of the limit: `f'(a) = lim(x -> a) (f(x) - f(a))/(x - a)` = `lim (x_1 -> x_2) (f(x_1) - f(x_2)) / (x_2 - x_1)`
        *   where  `x_2 = x` & `x_1 = a`.
    *   which is equivilent to `f'(a) = lim(h -> 0) (f(a + h) - f(a)) / h`. This definition is denoted increment notation.
    *   this alternative form is useful in richardson extrapolation

**example of approximating**
*   `h = h_0` => `f'(a) ~= (f(a + h_0) - f(a)) / h_0`
    *   `h = h_1 = h_0 / 2` => `f'(a) ~= (f(a + h_1) - f(a)) / h_1`
    *   If `h_k -> 0`, then we expect that `f'(a) = lim(k -> inf) (f(a + h_k) - f(a)) / h_k`.
* for some `k`: `|f'(a) - ((f(a + h_k) - f(a)) / h_k)|` will be a small enough error.

