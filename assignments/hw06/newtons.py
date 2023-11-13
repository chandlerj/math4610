import math

def newton(f, df, x0, err, maxIter):
    x1 = x0
    for _ in range(maxIter):
        fx1 = f(x1)
        if abs(fx1) < err:
            return x1
        dfx1 = df(x1)
        if dfx1 == 0:
            print("ERR: derivative is equal to zero")

            return None
        x1 = x1 - fx1 / dfx1
    print("ERR: maxIter reached. No solution available")
    return None

def f(x):
   return math.pow(x,2) - 5 * x + 6 

def df(x):
    return (2 * x) - 5

print(newton(f, df, 2.6, 0.01, 100))