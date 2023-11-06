# 0x0A. Python - Inheritance

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
