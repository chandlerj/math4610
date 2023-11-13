import math, newtons, bisection 


def hybrid(f, df, a, b, tol, maxIter):
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        print(f'invalid range: [{a},{b}]')
    
    err = 10.0 * tol
    iter = 0
    while(err > tol and iter < maxIter):
        iter += 1
        x0 = 0.5 * (a + b)
        x1 = x0 - (f(x0) / df(x0))

        if abs(x1 - x0) > (0.5 * (b - a)):
            c = x0
            fc = f(c)
            for _ in range(4):
               c = bisection.bisection(f, a, b, tol, 4) 

            x0 = c
        else:
            while(err < tol):
                newtons.newton(f, df, x0, err, maxIter)
    return x1

def f(x):
   return math.pow(x,2) - 5 * x + 6 

def df(x):
    return (2 * x) - 5

print(hybrid(f, df, 2.6, 3.3, 0.01, 100))