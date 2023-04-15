#!/usr/bin/python3
''' add_integer function '''


def add_integer(a, b=98):
    ''' adds two integers or floats '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
