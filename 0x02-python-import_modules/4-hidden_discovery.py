#!/usr/bin/python3
def main():
    with open('hidden_4.pyc', 'rb') as pyc_file:
        pyc_contents = pyc_file.read()

    # You now have the contents of the .pyc file in the 'pyc_contents' variable.
    for w in pyc_contents:
        # if not w[:2] == "__":
        print(w)


if __name__ == "__main__":
    main()
