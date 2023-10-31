#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = "-" if number < 0 else ""
if abs(number) % 10 > 5:
    message = "greater than 5"
elif abs(number) % 10 == 0:
    message = "0"
else:
    message = "less than 6 and not 0"
print(f"Last digit of {number} is {sign}{abs(number) % 10} and is {message}")
