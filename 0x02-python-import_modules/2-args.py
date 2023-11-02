#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv)
    print("{} {}{}".format(argc - 1,
          "argument" if argc == 2 else "arguments",
                           "." if argc == 1 else ":"))
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
