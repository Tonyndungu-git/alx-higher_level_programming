#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    for i in range(x):
        if i < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
            else:
                continue
        else:
            raise IndexError
        nb_print += 1
    print()
    return nb_print
