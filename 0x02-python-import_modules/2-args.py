#!/usr/bin/python3
import sys


def main(*argv):
    i = 0
    num_args = len(sys.argv) - 1
    if num_args == 1:
        print("{:d} argument:".format(num_args))
    elif num_args == 0:
        print("{:d} arguments.".format(num_args))
    else:
        print("{:d} arguments:".format(num_args))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    main()
