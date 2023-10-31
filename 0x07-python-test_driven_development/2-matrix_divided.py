#!/usr/bin/python3
"""This module divides all elements of a matrix
matrix must be a list of lists of integers or floats,
otherwise raise a TypeError
exception with the message matrix must be a matrix
(list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError
exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError
exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError
exception with the message division by zero
All elements of the matrix should be divided by div
, rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """This is a function that divides all elements of a matrix.
    Returns a new matrix.
    """
    new_matrix = []
    is_matrix_valid = all(
            isinstance(row, list) and all(
                isinstance(elem, (int, float)) for elem in row
            ) for row in matrix
        )
    if not is_matrix_valid:
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats'
                )
    matrix_len = len(matrix[0])
    if not all(len(row) == matrix_len for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for mat in matrix:
        new_list = []
        for m in mat:
            new_list.append(round((m / div), 2))
        new_matrix.append(new_list)
    return new_matrix
