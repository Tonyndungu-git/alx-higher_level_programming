#!/usr/bin/python3
''' Student class '''


class Student():

    def __init__(self, first_name, last_name, age):
        ''' initialization of the Student class '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        returns a dict data structure depending on the
        attributes defined

        '''
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict

    def reload_from_json(self, json):
        ''' that replaces all attributes of the Student instance '''
        for key, value in json.items():
            setattr(self, key, value)
