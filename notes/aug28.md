## First C Application

**hello.c**
```
#include <stdio.h>

int main()
{
    printf("Hello World!\n");
}
```

**compiling the application**

```
> gcc hello.c
```

*These instructions are OS agnostic*


## Introductary Algorithms

* matrix-matrix multiplication
* root finding methods
* power method for eigen systems
* Least squares fitting
* approximation of derivatives
    * We say `f` has a derivative at some `a` if the following limit exists:
        * `f'(x) = lim(h -> 0) (f(x + h) - f(x)) / h`
    * We can be approximate the derivative with a different quotient:
        * `f'(x) = (f(x + h) - f(x)) / h`. But how accurate is this approximation & how long does it take to compute? Additionally, how many funcions is this applicable for?
    * *def*: The error in approximating `f'(x)`, ` e ` can be measured using:
        *   `e = |f'(x) - ((f(x + h) - f(x)) / h)|`. where `h, e -> 0`.
        *   We can use the *taylor series* to analyze the behavior of this approximation.
            * Taylor series: `sum(n -> inf) ((f'(n) * a) / n!) (x - a)^n`
                *   `a` = Center of the series
                *   `f'(n)` = the nth derivative of f
        * wrapping it all together:
            * `f'(x) = f'(x)`
            * `f(x) = f(x)`
            * `f(x+h) = f(x) + (f'(x) / 1)(x+h * x)^1 + (f'(2)(x)/2) (x + h - x)^2 + ... + ((f'(n) * a) / n!) (x - a)^n`
            * `e_h = | -1/2 f'(x)h + ...|`
                * `e_h = |f'(x) - 1/h * (f(x) + f'(x)h + 1/2 * f'(2)(x)h - f(x))|`
                    * `= 1/2 h * |f'(2)(sig)`
                * this will allow us to test the accuracy of our approximation
            * 