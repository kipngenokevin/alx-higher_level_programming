#!/usr/bin/python3
"""This is a test module for the square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test the methods inside the Square"""

    def test_constructor(self):
        """Test the constructor method"""
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_default_values(self):
        """Test the default values"""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
    
    def test_str(self):
        """Test the __str__ function outputs correctly"""
        s = Square(4, 1, 2, 3)
        expected_output = "[Square] (3) 1/2 - 4"
        self.assertEqual(str(s), expected_output)

    def test_size_getter(self):
        """This test the getter method in square"""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """This test the setter method in square"""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_size_setter_with_validation(self):
        """Tests the getter and setter with validation"""
        square = Square(5)
        # Try to set size to a non-integer value, should raise a TypeError
        with self.assertRaises(TypeError):
            square.size = "invalid"

        # Try to set size to a non-positive value, should raise a ValueError
        with self.assertRaises(ValueError):
            square.size = 0
