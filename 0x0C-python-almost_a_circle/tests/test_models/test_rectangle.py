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
        self.assertEqual(r.id, 3)

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
        self.assertEqual(r.id, 4)
