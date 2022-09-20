#!/usr/bin/python3
"""
class called Rectangle

"""
class Rectangle:
    """
    initializing the height and width of a rectangle

    """
    def __init__(self, width="", height=""):
        self.width = width
        self.height = height

    @property
    def width(self):

        def width(self):
        """get rectangle width
        """
        return self.__width

    @property
    def height(self):
        """rectangle height
        """
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
