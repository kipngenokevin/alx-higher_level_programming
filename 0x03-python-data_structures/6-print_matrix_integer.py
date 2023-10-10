#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            i = 0
            for item in row:
                if i < len(row) - 1:
                    print("{:d}".format(item), end=" ")
                    i += 1
                else:
                    print("{:d}".format(item))
