#!/usr/bin/python3
import hidden_4


def main():
    args = dir(hidden_4)
    for i in range(len(args)):
        if (args[i][0] != '_'):
            print("{}".format(args[i]))


if __name__ == "__main__":
    main()
