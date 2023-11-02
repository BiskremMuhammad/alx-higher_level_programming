#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv)
    sum = 0
    for i in range(1, argc):
        sum += int(argv[i])

    print(sum)


if __name__ == "__main__":
    main()
