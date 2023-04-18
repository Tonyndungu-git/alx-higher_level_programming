#!/usr/bin/python3
''' class TestBase '''
import unittest
import json
from models import base
Base = base.Base

class TestBase(unittest.TestCase):
    ''' unittest of the base class '''
    def test_init(self):
        ''' testing the initialization '''
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(7)
        self.assertEqual(b2.id, 7)

    def test_to_json_string(self):
        ''' testing the to_json function '''
        b = Base(3)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 2}]), '[{"id": 2}]')

    def test_from_json_string(self):
        ''' testing the from_json function '''
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 3}]'), [{"id": 3}])

    def test_create(self):
        ''' testing the craete function '''
        b = Base(4)
        d = b.to_dictionary()
        b1 = Base.create(**d)
        self.assertEqual(str(b1), "[Base] (4) {}")

    def test_load_from_file(self):
        ''' testing the load_from_file function '''
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        l1 = Base.load_from_file()
        self.assertEqual(str(l1[0]), "[Base] (1) {}")
        self.assertEqual(str(l1[1]), "[Base] (2) {}")

if __name__ == '__main__':
    unittest.main()
