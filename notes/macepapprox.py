import numpy as np

eps = 1.0
one = 1.0
appone = one + eps

error = np.abs(appone - one)

for i in range(1000):
    print(error)
    eps = eps/2
    appone = one + eps
    error = np.abs(appone - one)
    if error == 0.0:
        break