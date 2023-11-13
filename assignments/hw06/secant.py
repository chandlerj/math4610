import math

def secant(f, a, b, matIter):
    fa = f(a)
    fb = f(b)

    if f(a) * f(b) >= 0:
        print("secant method failed.")
        return None
    for _ in range(1, matIter + 1):
        c = a - fa * (b - a)/(fb - fa)
        fc = f(c)

        if fa * fc < 0:
            b = c
            fb = fc
        elif fb * fc < 0:
            a = c
            fa = fc
        elif fc == 0:
            return c
        else:
            print("no solution found")
            return None
    return a - fa * (b - a) / (fb - fa)

def f(x):
   return math.pow(x,2) - 5 * x + 6 

print(secant(f, 2.5, 3.2, 10))