# 0x0A. Python - Inheritance
Inheritance is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class. 

## Resources
* [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
* [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
* [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
* [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

## Learning objectives
* Why Python programming is awesome
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Function that returns the list of available attributes and methods of an object
* Prototype: `def lookup(obj):`
* Returns a `list` object

**0-main.py**
```
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
```

**0-lookup.py**
```
#!/usr/bin/python3
""" This module contains a function
that returns the list of available attributes and methods
of an object
"""


def lookup(obj):
    """ Returns the available attributes and methods
    of an object.
    """
    return dir(obj)
```

## Class MyList that inherits from list
* Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
* You can assume that all the elements of the list will be of type `int`

**1-my_list.py**
```
#!/usr/bin/python3
""" This module with class MyList that inherits from list"""


class MyList(list):
    """ def print_sorted(self):
    that prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)
        all the elements of the list will be of type int
        """
        sorted_list = sorted(self)
        print(sorted_list)
```

The test cases - researched.

```
The ``1-my_list`` module
============================

Using ``1-mylist``
---------------------

Import function from module:
    >>> MyList = __import__('1-my_list').MyList

Correct Class Type test:
    >>> ml = MyList()
    >>> type(ml) == MyList
    True

Correct Instance test:
    >>> ml = MyList()
    >>> isinstance(ml, list)
    True

print_sorted method is an instance method:
    >>> type(MyList.__dict__['print_sorted'])
    <class 'function'>

print_sorted method called via class with no args:
    >>> ml.__class__.print_sorted()
    Traceback (most recent call last):
    TypeError: print_sorted() missing 1 required positional argument: 'self'

print_sorted method called with 1 arg:
    >>> ml.print_sorted([4, 2, 5])
    Traceback (most recent call last):
    TypeError: print_sorted() takes 1 positional argument but 2 were given

print_sorted method called with 2 args:
    >>> ml.print_sorted([4, 2, 5], 1)
    Traceback (most recent call last):
    TypeError: print_sorted() takes 1 positional argument but 3 were given

Empty list test:
    >>> ml = MyList()
    >>> ml.print_sorted()
    []

Normal list test:
    >>> ml = MyList([2, 10, 1])
    >>> ml.print_sorted()
    [1, 2, 10]

Normal list test 2:
    >>> ml = MyList([1, 4, 2, 3, 5])
    >>> ml.print_sorted()
    [1, 2, 3, 4, 5]

Negative ints list test:
    >>> ml = MyList([-1000, -98, -232565, 0, -23423434, -123])
    >>> ml.print_sorted()
    [-23423434, -232565, -1000, -123, -98, 0]

Original list unchanged:
    >>> ml = MyList([2, 10, 1, -10, 20, 100, 0])
    >>> ml.print_sorted()
    [-10, 0, 1, 2, 10, 20, 100]
    >>> ml
    [2, 10, 1, -10, 20, 100, 0]

List already in order:
    >>> ml = MyList([-10, 0, 1, 2, 10, 20, 100])
    >>> ml.print_sorted()
    [-10, 0, 1, 2, 10, 20, 100]

Test append:
    >>> ml = MyList()
    >>> ml.append(10)
    >>> ml
    [10]
```

## Function that returns True if the object is exactly an instance of the specified class
* Prototype: `def is_same_class(obj, a_class):`
**2-is_same_class.py**
```
#!/usr/bin/python3
""" module with function that
returns True of false depending on whether
an object is the instance of the class
"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly
    an instance of the specified class  otherwise, false
    """
    return type(obj) == a_class
```

***No Test Cases Needed***

Using `isinstance` is more versatile because it also considers subclasses. If you want to check whether an object is an instance of a specific class or any of its subclasses.

## Function that returns True if the object is an instance of...
function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
* Prototype: `def is_kind_of_class(obj, a_class):`

**3-is_kind_of_class.py**
```
#!/usr/bin/python3
"""This module demonstrates the use of isinstance"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the objec
    is an instance of a class that inherited from, the specified class
    otherwise False.
    """
    return isinstance(obj, a_class)
```

## Object is an instance of a class that inherited (directly or indirectly) from the specified class
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
* Prototype: `def inherits_from(obj, a_class):`

**4-inherits_from.py**
```
def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
    obj: The object to check.
    a_class: The class to check against.

    Returns:
    True if the object is an instance of a class that inherited from the specified class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
```

## An empty class BaseGeometry
**5-base_geometry.py**
```
class BaseGeometry:
    pass
```

## Class BaseGeometry
* Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
**6-base_geometry.py**
```
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
```

## Class BaseGeometry (based on 6-base_geometry.py)
* Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
* Public instance method: `def integer_validator(self, name, value):` that validates `value`
* you can assume `name` is always a string
* if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
* if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`

**7-base_geometry.py**
```
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
```

## Class Rectangle that inherits from BaseGeometry
* Instantiation with width and height: `def __init__(self, width, height):`
* `width` and `height` must be private. No getter or setter
* `width` and `height` must be positive integers, validated by integer_validator

**8-rectangle.py**
```
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
```

## Class Rectangle that inherits from BaseGeometry
* Instantiation with width and height: `def __init__(self, width, height):`
* `width` and `height` must be private. No getter or setter
* `width` and `height` must be positive integers, validated by integer_validator
* the `area()` method must be implemented
* `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

**9-rectangle.py**
```
#!/usr/bin/python3
"""Rectangle class Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initilize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
```

## Class Square that inherits from Rectangle
* Instantiation with size: `def __init__(self, size):`
* `size` must be private. No getter or setter
* `size` must be a positive integer, validated by `integer_validator`
* the `area()` method must be implemented

**10-square.py**
```
#!/usr/bin/python3
"""Square class Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Method for initializing a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns area of a square"""
        return self.__size ** 2
```
