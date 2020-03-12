import numpy as np

def SMC(v1 , v2):
    a = np.sum(v1 == v2)
    return (a / len(v1))


def SMC_1(v1 , v2):
    a = np.sum(v1 != v2)
    return 1- (a /( sum(v1)+ sum(v2) )   )

def SMC_2(v1 , v2):
    a = np.sum(v1 == v2)
    return np.power((a / len(v1)) , 3)