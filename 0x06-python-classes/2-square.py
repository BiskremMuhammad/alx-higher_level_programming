#!/usr/bin/python3
class Square:
    """constructor"""

    def __init__(self, size=0):
        """Initialises the size"""
        if not size.isdigit():
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
