#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height


        @property
        def width(self):
            return self.__width


        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("Width must be an integer")
            elif value < 0:
                raise ValueError("width must be greater than zero")
            else:
                self.__width = width


        @property
        def height(self, value):
            return self.__width


        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("width must be greater than zero")
            else:
                self.__height = height
