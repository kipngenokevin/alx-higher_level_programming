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

    def test_update_with_args(self):
        """This tests the update method with args"""
        square = Square(5, 1, 2, 3)
        square.update(10, 20, 30, 40)

        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_update_with_kwargs(self):
        """This test checks the update method with kwargs"""
        square = Square(5, 1, 2, 3)
        square.update(id=50, size=20, x=30, y=40)

        self.assertEqual(square.id, 50)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_update_with_args_and_kwargs(self):
        """This checks the update method with both args and kwargs"""
        square = Square(5, 1, 2, 3)
        square.update(10, 20, id=50, size=60)

        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_to_dictionary(self):
        """This method tests to dictionary method"""
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()

        expected_output = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_output)
