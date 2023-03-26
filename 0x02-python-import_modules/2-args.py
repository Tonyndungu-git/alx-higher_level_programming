#!/usr/bin/python3

import sys

# Get the command line arguments
args = sys.argv[1:]
num_args = len(args)

# Print the number of arguments and the list of arguments
if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
    print(f"1: {args[0]}")
else:
    print(f"{num_args} arguments:")
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
