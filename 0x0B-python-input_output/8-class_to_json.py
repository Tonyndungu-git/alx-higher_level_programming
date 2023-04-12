#!/usr/bin/python3
''' class_to_json function '''
import json


def class_to_json(obj):
    ''' retuns python data structure from json'''
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, float, str, bool)):
            json_dict[key] = value
        elif isinstance(value, list):
            json_list = []
            for item in value:
                if hasattr(item, '__dict__'):
                    json_list.append(class_to_json(item))
                else:
                    json_list.append(item)
                json_dict[key] = json_list
        elif isinstance(value, dict):
            json_dict[key] = {}
            for k, v in value.items():
                if hasattr(v, '__dict__'):
                    json_dict[key][k] = class_to_json(v)
                else:
                    json_dict[key][k] = v

    return json_dict
