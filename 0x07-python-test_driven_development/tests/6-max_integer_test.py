#!/usr/bin/python3
"""Unittest for the function max_integer[...]
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a class that will perform unittests
    on our function max_integer
    """

    def test_max_integer(self):
        """This is a function to run test cases on
        max_integer function.
        """
        # Test with positive integers only
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        # Test with list containing negative values
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        # Test with a list containing both positive and negative numbers
        self.assertEqual(max_integer([1, -2, 3, -4, 5]), 5)
        # Test with a list containing a single int
        self.assertEqual(max_integer([42]), 42)
        # Test with an empty list
        self.assertIsNone(max_integer([]))
        # Test with list containing duplicates
        self.assertEqual(max_integer([1, 3, 5, 5, 3, 1]), 5)
        # Test with list of large numbers
        self.assertEqual(max_integer([10**9, 10**9 + 1, 10**9 - 1]), 10**9 + 1)
        # Test with 2 integers where the first is larger
        self.assertEqual(max_integer([5, 3]), 5)
        # Test with the smaller integer coming in first
        self.assertEqual(max_integer([3, 5]), 5)
        # Test with a list containing a large number of elements
        self.assertEqual(max_integer(list(range(1, 10001))), 10000)
        # Test with a list of floats, where the maximum is an integer
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0, 5.0]), 5)
        # Test with a list of floats, where the maximum is a float
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4, 5.5]), 5.5)
        # Test with a list containing non-integer and non-float values
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), 'cherry')
        # Test with a list of boolean values
        self.assertEqual(max_integer([True, False, True]), True)
        # Test with a list of mixed data types,
        self.assertEqual(max_integer([1, 2.0, True, 3, False, 4.4]), 4.4)
