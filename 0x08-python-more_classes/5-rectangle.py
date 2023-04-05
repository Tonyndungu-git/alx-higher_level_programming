#!/usr/bin/python3
'''module class'''


class Rectangle:
    ''' class Rectangle'''
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
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("width must be greater than zero")
        else:
            self.__width = value

    @property
    def height(self, value):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be greater than zero")
        else:
            self.__height = value

    def area(self):
        '''area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''perimeter of the rectangle'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height)+(2 * self.__width)

    def __str__(self):
        ''' prints stirngs of height and width of # '''
        if self.__width == 0 or self.__height == 0:
            return ""
        r = ""
        for i in range(self.__height):
            r += "#" * self.width + "\n"
        return r[:-1]

    def __repr__(self):
        '''helps  return a string representation of the object that can be used
        to recreate a new instance'''
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        ''' deletes and prints out a string '''
        print("Bye rectangle...")
