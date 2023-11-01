#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))
print('--')
print(Rectangle(10))
print(repr(my_rectangle))
print('Test 1 Fail')
myrectangle = Rectangle(2, 4)
Rectangle(2, 4) 
print(str(myrectangle))
print('end')
