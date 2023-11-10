#!/usr/bin/python3
"""This module performs unittest on the rectangle module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This is class to run test cases on Rectangle"""

    def test_constructor(self):
        """Test the constructor of Rectangle"""
        r = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 1)

    def test_default_values(self):
        """Test the constructor with default values"""
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 4)

    def test_setters(self):
        """Test the setters of a rectangle"""
        r = Rectangle(10, 20)
        r.width = 30
        r.height = 40
        r.x = 5
        r.y = 10

        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 5)

    def test_width_type_error(self):
        """This checks for TypeError of the width"""
        with self.assertRaises(TypeError) as context:
            r = Rectangle("Invalid", 20)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_value_error(self):
        """This checks for ValueError of the width"""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 20)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_x_type_error(self):
        """This checks for TypeError for x"""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 20, 'str', 5)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_value_error(self):
        """This checks for ValueError for x"""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 20, -2, 5)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y_type_error(self):
        """This checks for TypeError for y"""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 20, 5, 'str')
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_value_error(self):
        """This checks for ValueError for y"""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 20, 2, -5)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_height_type_error(self):
        """Test if TypeError is raised for invalid height type"""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, "invalid")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_value_error(self):
        """Test if ValueError is raised for invalid height value"""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_area(self):
        """Test the area method for correct output"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)
