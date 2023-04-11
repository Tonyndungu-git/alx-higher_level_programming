#!/usr/bin/python3
''' class BaseGeometry '''


class BaseGeometry:
    ''' class representing base geometry '''
    def area(self):
        ''' raises exception there is no area '''
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        ''' raises an exception depending on error '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
