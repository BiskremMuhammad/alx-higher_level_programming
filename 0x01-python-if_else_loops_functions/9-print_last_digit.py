#!/usr/bin/python3
def print_last_digit(number):
    sign = "-" if number < 0 else ""

    return sign + abs(number) % 10
