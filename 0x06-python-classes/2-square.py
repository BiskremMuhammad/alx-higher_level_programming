#!/usr/bin/python3
"""
a Square Class definition
"""


class Square:
    def __init__(self, size=0):
        """constructor"""
        self.__size = size
        if not type(size) is int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
