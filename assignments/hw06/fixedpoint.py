import math
import numpy as np
def fixedPoint(f, g, x0, err, maxIter):
    x1 = g(x0)
    iter = 0
    while abs(f(x1)) > err and iter < maxIter:
        print(f'iteration {iter} - x1: {x1}')
        x1 = g(x0)
        x0 = x1
        iter += 1
    return x1

def fixedPoint_scaled_helper(f, g, scale, x0, err, maxIter):
    x1 = g(x0, scale)
    iter = 0
    while abs(f(x1)) > err and iter < maxIter:
        print(f'iteration {iter} - x1: {x1}')
        x1 = g(x0, scale)
        x0 = x1
        iter += 1
    return x1

def findFixedPoint_q2(f, x0, err, maxIter):
    curr_scaler = 0.1
    curr_root = 0
    for i in range(maxIter):
        print(f'current scaler: {curr_scaler}')
        curr_root = fixedPoint_scaled_helper(f, g_3,curr_scaler, x0, err, maxIter)
        curr_scaler *= 2
    return curr_root

def f(x):
   return math.pow(x,2) - 5 * x + 6 
def g(x):
    return -6 / (x - 5) 
def g_1(x):
    return x + f(x)
def g_2(x):
    return x - f(x)
def g_3(x, scale):
    return x - (scale * f(x))



def main():
    root = fixedPoint(f, g, 2.4, 0.001, 10)
    print(f'the root of our f(x) using fixed point iteration with g(x) = x: {root}')
    root2 = fixedPoint(f, g_1, 2.4, 0.001, 10)
    print(f'the root of our f(x) using fixed point iteration with g(x) = x + fx: {root2}')
    root3 = fixedPoint(f, g_2, 2.4, 0.001, 10)
    print(f'the root of our f(x) using fixed point iteration with g(x) = x - fx: {root3}')

    print("----- Testing for Question 2 ------")
    root4 = findFixedPoint_q2(f, 2.4, 0.001, 5)
    print(f'root after iterating scaler values: {root4}')

   #print(f'the root of our f(x) using the root finding method from class is {root_v2}')



main()