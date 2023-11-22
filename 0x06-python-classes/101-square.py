#!/usr/bin/python3
"""
a Square Class definition
"""


class Square:
    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """constructor"""
        if not type(size) == int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        if (len(position) != 2 and
            type(position[0]) is not int and
                type(position[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

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

    @property
    def position(self):
        """retreive position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """position att setter"""

        if (len(value) != 2 and
            type(value[0]) is not int and
                type(value[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """print a square shape"""
        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

        if self.__size <= 0:
            print()

    def __str__(self):
        """default print square"""

        result = ""
        for i in range(self.__position[1]):
            result += "\n"

        for i in range(self.__size):
            for j in range(self.__position[0]):
                result += " "
            for j in range(self.__size):
                result += "#"

            result += "\n"

        if self.__size <= 0:
            result += "\n"

        return result

    def area(self):
        """claculate square area"""
        return self.__size ** 2
