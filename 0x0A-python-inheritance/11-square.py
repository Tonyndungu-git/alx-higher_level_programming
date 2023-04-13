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


''' subclass Rectangle '''


class Rectangle(BaseGeometry):
    ''' class defining a rectangle and its methods '''
    def __init__(self, width, height):
        '''initialization of the class Rectangle '''
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' Area of the class Rectangle '''
        return self.__width * self.__height

    def __str__(self):
        ''' printing of the height and width of class rectangle '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


''' subsubclass Square '''


class Square(Rectangle):
    ''' subsubclass square, inheriting from rectangle '''
    def __init__(self, size):
        ''' initialization of the subsubclass Square '''
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        ''' prints a string of the size '''
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        ''' area of a square '''
        return self.__size ** 2
