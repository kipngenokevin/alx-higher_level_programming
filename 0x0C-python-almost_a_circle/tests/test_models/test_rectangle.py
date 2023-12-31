#!/usr/bin/python3
"""This module performs unittest on the rectangle module"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


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
        self.assertEqual(r.id, 2)

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

    def test_display(self):
        """Test the display method for correct output"""
        r = Rectangle(3, 4)
        # redirect stdout to print output
        captured_output = StringIO()
        sys.stdout = captured_output

        r.display()

        # Reset redirect
        sys.stdout = sys.__stdout__

        # check if the output matches
        expected_output = "###\n###\n###\n###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        # New rectangle with x and y variables
        p = Rectangle(3, 4, 1, 2)
        # redirect to print to stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        p.display()
        # Reset redirect
        sys.stdout = sys.__stdout__
        # check if the output matches
        expected_output = '\n\n ###\n ###\n ###\n ###\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        """Test the __str__ function outputs correctly"""
        r = Rectangle(3, 4, 1, 2, 12)

        # Redirect to print to the output
        captured_output = StringIO()
        sys.stdout = captured_output

        print(r)

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check if output matches expected output
        expected_output = "[Rectangle] (12) 1/2 - 3/4\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update_all_attributes(self):
        """Test updating all attributes at once"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_partial_attributes(self):
        """Test updating only some attributes"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 3)  # x remains unchanged
        self.assertEqual(r.y, 4)  # y remains unchanged

    def test_update_no_attributes(self):
        """Test updating with no arguments"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_too_many_attributes(self):
        """Test updating with more arguments than attributes"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50, 60)  # 60 will be ignored
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_with_kwargs(self):
        """Test updating attributes with **kwargs"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 5)  # id remains unchanged
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_with_args_and_kwargs(self):
        """Test updating attributes with both *args and **kwargs"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_extra_kwargs_ignored(self):
        """Test updating with extra **kwargs that are not attributes"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(extra_attribute=100)
        self.assertEqual(r.id, 5)  # id remains unchanged
        self.assertEqual(r.width, 1)  # width remains unchanged
        self.assertEqual(r.height, 2)  # height remains unchanged
        self.assertEqual(r.x, 3)  # x remains unchanged
        self.assertEqual(r.y, 4)  # y remains unchanged

    def test_to_dictionary(self):
        """Tests to_dictionary method in class rectangle"""
        r = Rectangle(10, 20, 3, 4, 1)
        rectangle_dict = r.to_dictionary()

        expected_dict = {'id': 1, 'width': 10, 'height': 20, 'x': 3, 'y': 4}
        self.assertEqual(rectangle_dict, expected_dict)
