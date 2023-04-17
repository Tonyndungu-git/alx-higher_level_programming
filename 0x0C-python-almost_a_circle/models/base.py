#!/usr/bin/python3
''' class Base'''
import json
import csv


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        ''' initializes the base class and gives id '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns the JSON string representation of a list '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes a file as a json string '''
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        dictionary_list = []
        for obj in list_objs:
            dictionary_list.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(dictionary_list))

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string '''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' returns an instance with all attributes already set '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy is not None:
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_string = f.read()
                obj_list = cls.from_json_string(json_string)
                instance_list = []
                for obj in obj_list:
                    instance = cls.create(**obj)
                    instance_list.append(instance)
                return instance_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' save list_obj in csv format into a csv file '''
        filename = cls.__name__ + ".csv"

        with open(filename, "w") as f:
            w = csv.writer(f)
            if cls.__name__ == "Rectangle":
                w.writerow(["id", "width", "height", "x", "y"])
                for obj in list_objs:
                    w.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                w.writerow(["id", "size", "x", "y"])
                for obj in list_objs:
                    w.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                header = next(reader)
                objs = []
                for row in reader:
                    data = [int(x) for x in row]
                    obj = cls.create(**dict(zip(header, data)))
                    objs.append(obj)
                return objs
        except FileNotFoundError:
            return []
