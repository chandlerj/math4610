import numpy as np
import matplotlib.pyplot as plt

def function(x, ich):
    if ich==1:
        fval = x * np.exp(-x)
    if ich==2:
        fval = x * np.sin(2*x)
    return fval