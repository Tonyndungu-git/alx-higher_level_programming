#!/usr/bin/python3
'''This module contains the Square class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''A class named Square'''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Initializes a Square instance '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' Returns a string representation of the object'''
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        ''' getter method for size '''
        return self.width

    @size.setter
    def size(self, value):
        ''' setter method for size '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

        self.height = value

    def update(self, *args, **kwargs):
        ''' updates subclass square attributes with arguments '''
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' returns dictionary representation '''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
