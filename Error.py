import numpy as np
import Norm


def AbsoluteNorm1(a, b):
    if len(a) != len(b):
        print("Dimension of vectors is not equal!")
        return 0
    return Norm.NormP(np.array(a) - np.array(b), 1)


def AbsoluteNorm2(a, b):
    if len(a) != len(b):
        print("Dimension of vectors is not equal!")
        return 0
    return Norm.NormP(np.array(a) - np.array(b), 2)


def AbsoluteNormInf(a, b):
    if len(a) != len(b):
        print("Dimension of vectors is not equal!")
        return 0
    return Norm.NormInf(np.array(a) - np.array(b))


def AbsoluteNormP(a, b, p):
    if len(a) != len(b):
        print("Dimension of vectors is not equal!")
        return 0
    return Norm.NormP(np.array(a) - np.array(b), p)


def RelativeNorm1(a, b):
    if len(a) != len(b):
        print("Dimension of vectors is not equal!")
        return 0
    return Norm.NormP(np.array(a) - np.array(b), 1) / Norm.NormP(a, 1)


def RelativeNorm2(a, b):
    if len(a) != len(b):
        print("Dimension of vectors is not equal!")
        return 0
    return Norm.NormP(np.array(a) - np.array(b), 2) / Norm.NormP(a, 2)


def RelativeNormInf(a, b):
    if len(a) != len(b):
        print("Dimension of vectors is not equal!")
        return 0
    return Norm.NormInf(np.array(a) - np.array(b)) / Norm.NormInf(a)


def RelativeNormP(a, b, p):
    if len(a) != len(b):
        print("Dimension of vectors is not equal!")
        return 0
    return Norm.NormP(np.array(a) - np.array(b), p) / Norm.NormP(a, p)


def Relative(a, b):
    if a == 0:
        return 0
    return abs((a - b)) / abs(a)


def Absolute(a, b):
    return abs(a - b)
