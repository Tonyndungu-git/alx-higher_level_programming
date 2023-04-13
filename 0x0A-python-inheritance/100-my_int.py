#!/usr/bin/python3
''' subclass MyInt '''


class MyInt(int):
    ''' returns opposite of equal '''
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        ''' returns opposite of not equal '''

        return super().__eq__(other)
