#!/usr/bin/python3
''' add_item function '''

import sys
import json
from os import path
from typing import List

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args: List[str]):
    ''' add, load and then save to a file '''
    filename = "add_item.json"

    if path.isfile(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == '__main__':
    add_item(sys.argv[1:])
