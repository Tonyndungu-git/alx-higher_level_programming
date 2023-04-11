#!/usr/bin/python3
''' class BaseGeometry '''


class BaseGeometry:
    ''' class representing base geometry '''
    def area(self):
        ''' raises exception there is no area '''
        raise Exception("area() is not implemented")
