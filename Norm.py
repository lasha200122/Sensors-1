import numpy as np


def NormInf(x):
    return max([abs(i) for i in x])


def NormP(x, p):
    if p == "inf":
        return NormInf(x)
    return np.power(sum([np.power(abs(i), p) for i in x]), 1/p)
