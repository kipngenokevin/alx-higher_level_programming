#!/usr/bin/python3
"""This module is a technical interview question """


def pascal_triangle(n):
    """This performs the pascal triangle"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                # Calculate the elements in the current row
                # based on the previous row
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
