#!/usr/bin/python3
def print_last_digit(number):
    sign = -1 if number < 0 else 1
    print(sign * abs(number) % 10, end="")
    return sign * abs(number) % 10
