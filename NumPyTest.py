import numpy as np

def np_sum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

print(np_sum(10))