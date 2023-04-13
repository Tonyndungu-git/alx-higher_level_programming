#!/usr/bin/python3
''' append_after fuction '''


def append_after(filename="", search_string="", new_string=""):
    ''' appends a line new string after a specific line is read '''
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
