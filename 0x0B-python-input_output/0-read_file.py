#!/usr/bin/python3
''' function read_file '''


def read_file(filename=""):
    ''' reads a text file '''
    with open(filename, 'r', encoding='utf8') as f:
        text = f.read()
    print(text)
