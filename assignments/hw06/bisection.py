import math

def bisection(f, a, b, tol, maxIter):
    fa = f(a)
    fb = f(b)
    c = 0
    err = 10 * tol
    if fa == 0:
        return a
    elif fb == 0:
        return b
    if fa * fb >= 0:
        print("root cannot be guranteed on this interval")
        return None
    
    #k = int(np.emath.logn(2, tol / b - a) / np.emath.logn(2, 1/2)) + 1
    #print(k)
    #for i in range(k):
    iterCount = 0
    while err > tol and iterCount < maxIter:
        c = (a + b) / 2 
        fc = f(c)
        if fc == 0:
            break
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        err = b - a
        iterCount += 1
    return c

def f(x):
   return math.pow(x,2) - 5 * x + 6 

print(bisection(f, 2.5, 3.5, 0.001, 1000))