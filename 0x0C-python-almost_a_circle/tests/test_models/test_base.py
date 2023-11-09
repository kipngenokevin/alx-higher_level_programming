#!/usr/bin/python3
"""This is a unittest module to test the  base class"""
import unittest
from models.base import Base


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
