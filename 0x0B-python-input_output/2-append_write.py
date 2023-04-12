#!/usr/bin/python3
''' append_write function '''


def append_write(filename="", text=""):
    ''' appends into a file '''
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
