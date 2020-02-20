import numpy as np

def SMC(v1 , v2):
    a = np.sum(v1 == v2)
    return a / len(v1)