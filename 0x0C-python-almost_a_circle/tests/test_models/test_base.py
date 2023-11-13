#!/usr/bin/python3
"""This is a unittest module to test the  base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
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

    @classmethod
    def setUpClass(cls):
        """# Create a temporary file with some data"""
        cls.temp_file = "Rectangle.json"
        data = (
                '[{"id": 1, "width": 3, "height": 4, "x": 0, "y": 0}, '
                '{"id": 2, "width": 5, "height": 6, "x": 0, "y": 0}]')
        with open(cls.temp_file, 'w', encoding='utf-8') as file:
            file.write(data)

        cls.temp_file_square = "Square.json"
        data_square =(
                '[{"id": 3, "size": 2, "x": 1, "y": 1}, '
                '{"id": 4, "size": 4, "x": 2, "y": 2}]')
        with open(cls.temp_file_square, 'w', encoding='utf-8') as file_square:
            file_square.write(data_square)

    @classmethod
    def tearDownClass(cls):
        """Remove the temporary file"""
        os.remove(cls.temp_file)

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
        """Test the save_to_file class method"""
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

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        result = Base.from_json_string('')
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        string = '[{"id": 1, "width": 3, "height": 4, "x": 0, "y": 0}]'
        result = Base.from_json_string(string)
        expected = [{"id": 1, "width": 3, "height": 4, "x": 0, "y": 0}]
        self.assertEqual(result, expected)

    def test_create_rectangle(self):
        """Test create with a rectangle instance"""
        rectangle_dict = {'width': 4, 'height': 6, 'id': 1}
        rectangle_instance = Rectangle.create(**rectangle_dict)

        self.assertIsInstance(rectangle_instance, Rectangle)
        self.assertEqual(rectangle_instance.width, 4)
        self.assertEqual(rectangle_instance.height, 6)
        self.assertEqual(rectangle_instance.id, 1)

    def test_create_square(self):
        """Test create with a square instance"""
        square_dict = {'size': 3, 'id': 2}
        square_instance = Square.create(**square_dict)

        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.size, 3)
        self.assertEqual(square_instance.id, 2)

    def test_create_with_invalid_keys(self):
        """Test create with invalid keys"""
        invalid_dict = {'invalid_key': 42}

        with self.assertRaises(TypeError):
            Base.create(**invalid_dict)

    def test_load_from_file(self):
        """Test loading instances from the temporary file"""
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertIsInstance(instances[1], Rectangle)
        self.assertEqual(instances[0].width, 3)
        self.assertEqual(instances[1].height, 6)

    def test_load_from_file_nonexistent_file(self):
        """Test loading from a nonexistent file"""
        os.remove("Square.json")
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 0)
