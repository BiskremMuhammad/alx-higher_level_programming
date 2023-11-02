#!/usr/bin/python3
import sys


def main():
    print("{} arguments:".format(len(sys.argv)))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i - 1]))


if __name__ == "__main__":
    main()
