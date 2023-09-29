<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>


*September 25: Still talking about approximating derivatives edition*

**Ex:** Approximate $$erfc(x) = \int_0^x \frac{2}{\sqrt{\pi}} e^{-t^2} dt$$


**Def:** explicit Euler Method - $$\frac{P(t + \Delta t) - P(t)}{\Delta t} \approx P(t) - \Beta P^2(t)$$

Using `log` to determine error:

$$\log(e_h) = \log(c) + r\log(h_m)\\y_k = a + rx_m$$

Using the log allows us to project into the plane of normal equations and perform a regression. 

**Notes for implementing this in code**
*   `A^TA` is symmetric
*   `A` is an element of the 2x2 matrices
*   we can compute the inverse of `A` since it is a 2x2 matrix

**Pseudo code**
```
Input: x: list, y, n

a_11 = n+1

a_12 = x[0]

a_21 = a_12

a_22 = x[0] * x[0]

for i in range(n):
    a_12 = a_12 + x[i + 1]
    a_22 = a_22 + x[i + 1] * x[i + 1]
a_21 = a_12

b_1 = y[0]
b_2 = y[0] * x[0]

for i in range(n):
    b_1 = b_1 + y[i + 1]
    b_2 = b_2 + y[i + 1] * x[i + 1]

detA = a_22 * a_11 - a_12 * a_21

c = (a_22 * b_1 - a_12 * b_2) / detA

d = (-a_21 * b_1 + a_11 * b_2) / detA

return (c, d)
```

**Test:** $$f(x) = x e^{-x^2}$$

assume that `f'(x)` is not available. We can still compute the approximation as h varies:

$$(h_0, df(h_0))\\(h_1, df(h_1))\\...\\(h_n, df(h_n))$$

We want: 

$$e_{k} = |df(h_k) - f'(a)| = |df(h_k) - df(h_m) + df(h_m) - f'(a) |\\ \leq |df(h_m) - df(h_m)| + |df(h_m) - f'(a)|$$


*September 27*

*Last commment on previous material*

* We can use these ideas (approximating and testing derivatives, roundoff error, taylor series, etc) on problems where the answer is unknown. 
