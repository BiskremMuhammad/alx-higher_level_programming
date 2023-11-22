#!/usr/bin/python3
"""
a Square Class definition
"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """constructor"""
        self.__size = size
        if not type(size) == int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """retreive size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """size att setter"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """claculate square area"""
        return self.__size ** 2
