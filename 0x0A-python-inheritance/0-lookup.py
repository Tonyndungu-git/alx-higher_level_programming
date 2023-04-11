#!/usr/bin/python3
''' lookup function'''


def lookup(obj):
    ''' returns the list of available attributes and methods of an object'''
    mylist = dir(obj)
    return mylist
