#!/usr/bin/python3
'''module class'''


class Rectangle:
    def __init__(self, width=0, height=0):
        '''initialization of class Rectangle'''
        self.width = width
        self.height = height

        @property
        def width(self):
            '''width getter returns private width'''
            return self.__width

        @width.setter
        def width(self, value):
            '''width setter'''
            if not isinstance(value, int):
                raise TypeError("Width must be an integer")
            elif value < 0:
                raise ValueError("width must be greater than zero")
            else:
                self.__width = width

        @property
        def height(self, value):
            '''height getter'''
            return self.__width

        @height.setter
        def height(self, value):
            '''height setter '''
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("width must be greater than zero")
            else:
                self.__height = height
