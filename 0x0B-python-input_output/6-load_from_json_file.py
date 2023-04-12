#!/usr/bin/python3
''' load_from_json_file function'''
import json


def load_from_json_file(filename):
    '''reads a json file '''
    with open(filename, 'r') as f:
        object = json.load(f)
    return object
