#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    else:
        matrix_2 = []
        for row in matrix:
            new_matrix = []
            for item in row:
                new_matrix.append(item ** 2)
            matrix_2.append(new_matrix)
        return matrix_2
