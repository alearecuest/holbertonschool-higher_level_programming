#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row_path in matrix:
        for n in range(len(row_path)):
            if n < len(row_path) - 1:
                print("{:d}".format(row_path[n]), end=" ")
            else:
                print("{:d}".format(row_path[n]), end="")
        print()
