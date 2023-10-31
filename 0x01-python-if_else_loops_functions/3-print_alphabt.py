#!/usr/bin/python3
for i in range(ord("a"), ord("z") + 1):
    if not chr(i) in "qe":
        print("{}".format(chr(i)), end="")
