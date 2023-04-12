#!/usr/bin/python3
''' save_to_json_file function'''
import json


def save_to_json_file(my_obj, filename):
    ''' saves an object as a json file '''
    with open(filename, 'w') as f:
