#!/usr/bin/python3

def uniq_add(my_list=[]):
    n = 0
    uniq_no = set(my_list)
    for i in uniq_no:
        n += i
    return n
