#!/usr/bin/python3
''' add_attr function '''
def add_attribute(obj, attr, value):
    '''  adds an attribute if an object doesn't have one '''
    if hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
