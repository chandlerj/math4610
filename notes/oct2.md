<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>

# math 4610: *cock*tober 2
*spooky version*

the error function `erf` is defined as:
$$ erf(x) = \int_0^x \frac{2}{\sqrt{\pi}} e^{-s^2} ds$$

*ex* (of expanding the central diff theorem): 
$$
f'(a) \approx \frac{f(a+h) - f(a - h)}{2h}\\

f(a + h) = f(a) - f'(a) f'(a)h + \frac{f''(\xi)}{2!}h^2\\
f(a - h) = f(a) -f'(a)h + \frac{f''(\xi)}{2!} h^2\\

error = |f'(a) - \frac{1}{h} (0 + 2hf'(a) + \frac{f''(\xi)}{2!} h^2 - \frac{f''(\xi)}{2!} h^2) |\\

= | (\frac{f'(\xi_+) - f'(\xi_-)}{2!}) \frac{h}{2}  | \leq Ch^1
$$


## Upcoming topics in FCM
*   Direct solutions of linear systems using gauess elimination
*   Iterative solutions of linear systems
    *   Jacobi iteration
*   find the largest eigenvalue and magnitude for any matrix.
    *   will use power method to accomplish this
*   Time stepping methods for first order ODEs.
    *   Ex `y' = f(t + y) & y'(t_0) = y_0)`
*   FFTs - Fast forey transfers


## Solutions of linear systems using direct methods

Theoretially, every method we apply will be an equivalent operation and produce identical results, but in actuality there are differences due to roundoff errors and the finite nature of computers.

### Gaussian Elimination

*Problem Description*: Given matrix `A in R^(n x n)`and `b in R^n`, find `x in R^n` such that `Ax = b`.

*Example*: 
$$ 2x - 5y = 7 \\ 3x + 7y = 12 $$

we can then construct a table to perform guarssian elimination:



a general system for solving these equations is:
$$ a_{11} x_1 + a_{12} x_2 + a_{13} x_3 + ... + a_{1n} x_n = b_1\\ a_{21} x_1 + a_{22} x_2 + a_{23} x_3 + ... + a_{2n} x_n = b_2\\ ...\\\
a_{n1} x_1 + a_{n2} x_2 + a_{n3} x_3 + ... + a_{nn} x_n = b_n$$

We can then convert this system to a matrix with the matrix `A` containing the values `a_nn`, the vector `x` which contains the `x_n` values, and the vector `b` which is the `b_n` on the RHS.

