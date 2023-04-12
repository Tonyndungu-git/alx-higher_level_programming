#!/usr/bin/python3
''' write_file function '''


def write_file(filename="", text=""):
    ''' function that writes into a file '''
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
