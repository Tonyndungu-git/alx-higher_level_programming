#!/usr/bin/python3

def magic_calculation(a, b):
    c = 0
    if a > b:
        c = a + b
    else:
        for i in range(b):
            c += a + i
    return c
