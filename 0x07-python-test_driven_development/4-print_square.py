#!/usr/bin/python3
''' print_square function'''


def print_square(size):
    ''' Prints a square of '#' characters of a given size.'''
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
