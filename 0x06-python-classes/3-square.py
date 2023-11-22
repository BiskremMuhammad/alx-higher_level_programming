#!/usr/bin/python3
class Square:
    """constructor"""

    def __init__(self, size=0):
        """Initialises the size"""
        self.__size = size
        if not type(size) == int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size ** 2
