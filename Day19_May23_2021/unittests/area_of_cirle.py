from math import pi


def area_of_circle(r):
    if isinstance(r, str) or isinstance(r, complex) or isinstance(r, bool):
        raise TypeError
    if r < 0:
        raise ValueError
    return pi * r * r