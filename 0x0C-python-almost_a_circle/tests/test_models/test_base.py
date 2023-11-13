#!/usr/bin/python3
"""This is a unittest module to test the  base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os
import textwrap


class TestBaseClass(unittest.TestCase):
    """ This class will perform tests on my base class"""

    def setUp(self):
        """ Setup resources for testing """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Tear down resources after use """
        pass

    def test_constructor_no_id(self):
        """Test constructor when no id is provided"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_constructor_with_id(self):
        """Test constructor when id is provided"""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_constructor_with_multiple_objects(self):
        """Test constructor with multiple objects"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_string_empty_list(self):
        """Test the json to string method with an empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        """Test the json to string function with a None Value"""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        """Test the json to string with a list with dictionaries"""
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        result = Base.to_json_string(data)
        expect = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(result, expect)

    def test_save_to_file(self):
        # Create instances
        r1 = Rectangle(3, 4)
        r2 = Rectangle(5, 6)

        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", 'r') as file:
            content = file.read()
            expect = (
                    '[{"id": 1, "width": 3, "height": 4, "x": 0, "y": 0}, '
                    '{"id": 2, "width": 5, "height": 6, "x": 0, "y": 0}]')
            self.assertEqual(content.strip(), expect)
