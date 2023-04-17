#!/usr/bin/python3
''' class Rectangle '''
from models.base import Base


class Rectangle(Base):
    '''initializing the class rectangle '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''function to initialize  the rectangle class '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' getter method for width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setter method for width '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' getter method for height'''
        return self.__height

    @width.setter
    def height(self, value):
        ''' setter method for height '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        ''' getter method for x '''
        return self.__x

    @width.setter
    def x(self, value):
        ''' setter method for x '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        ''' getter method for y '''
        return self.__y

    @width.setter
    def y(self, value):
        ''' setter method for y '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        ''' area function nof the rectangle class '''
        return self.__width * self.__height

    def display(self):
        '''print rectangle with offsets'''
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print("", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        '''return string representation'''
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        ''' Assigns arguments args and kwargs to each attribut using attr '''
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for attrs, value in zip(attrs, args):
                setattr(self, attrs, args)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' returns dictionary representation '''
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
