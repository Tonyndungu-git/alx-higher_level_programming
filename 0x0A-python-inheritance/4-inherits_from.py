#!/usr/bin/python3
'''inherits_from function'''


def inherits_from(obj, a_class):
    ''' function that returns True if the object inherited a class'''
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
