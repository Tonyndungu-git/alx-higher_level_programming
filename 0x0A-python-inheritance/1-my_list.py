#!/usr/bin/python3
''' subclass MyList '''


class MyList(list):
    ''' prints a sorted list '''
    def print_sorted(self):
        ''' prints a sorted list '''
        sorted_list = sorted(self)
        print(sorted_list)
