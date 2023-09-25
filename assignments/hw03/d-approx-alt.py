#
# the code in this file will approximate the derivative of a "smooth" function
# using a forward difference
#
# storage
import numpy as np
import matplotlib.pyplot as plt
#
#
# test function for computing derivatives
#
# the derivative
# --------------
#
def f(x):
    fval = x * np.exp(-x)
    return fval
#
# the exact derivative expression
# -------------------------------
#
def df(x):
    dfval = np.exp(-x) - x * np.exp(-x)
    return dfval
#
# the difference quotient for the derivative approximation
# --------------------------------------------------------
#
def dfapp(x, h):
    appval = ( f(x+h) - f(x) ) / h
    return appval
#
# location for the derivative along with an array for increment to use in the
# approximation and an array to store the error for each value tested
# -------------------------------------------------------------------
#
x0 = 1.2
napprox = 50
h = []
error = []
#
# initialize the increment to do the initial approximation
# --------------------------------------------------------
#
hval = 1.0
#
# compute the "exact" derivative
# ------------------------------
#
dfexct = df(x0)
#
# loop over i for generating a list of approximate values
# -------------------------------------------------------
#
for i in range(napprox):
    #
    # compute the difference quotient for the function
    # ------------------------------------------------
    #
    dfappr = dfapp(x0, hval)
    #
    # compute the approximate error between the "exact" value and the approximate
    # value
    # -----
    errval = np.abs(dfappr-dfexct)
    #
    # store the value of the increment and the error for use below
    # ------------------------------------------------------------
    #
    h.append(hval)
    error.append(errval)
    #
    # update the increment by reducing the increment by one half
    # ----------------------------------------------------------
    #
    hval = hval / 2
        #
    # print each of the raw data value for the current index, i, increment,
    # hval,and the current error, error[i]
    # ------------------------------------
    #
    print(i, h[i], error[i])
#
# the rest of the code will bring up a graphical representation of the error
# as a function of the increment, h.
# ----------------------------------
#
plt.plot(h, error)
plt.title("Graph of Error in Derivative Approximation")
plt.xlabel("h (Increment Value)")
plt.ylabel("error (Error in Derivative Approximation)")
plt.show()