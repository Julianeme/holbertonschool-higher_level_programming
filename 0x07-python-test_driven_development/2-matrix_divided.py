#!/usr/bin/python3
"""
    Returns the result dividing each value of matrix
    by the div value. works only with integers and floats
    div value should be diff than zero
"""


def matrix_divided(matrix, div):
    """
        Returns the input matrix divided by div variable
    """

    new_matrix = []
    mess1 = "Each row of the matrix must have the same size"
    mess2 = "matrix must be a matrix (list of lists) of integers/floats"
    if len(matrix) > 1:
        length_matrix = len(matrix[0])

    for row in range(len(matrix)):
        for num in matrix[row]:
            if type(num) is not int and type(num) is not float:
                raise TypeError(mess2)
            if len(matrix[row]) != length_matrix:
                raise TypeError(mess1)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise ZeroDivisionError("div must be a number")

    for row in range(len(matrix)):
        new_matrix.append([])
    for row in range(len(matrix)):
        for num in matrix[row]:
            new_matrix[row].append(round((num / div), 2))
    print(new_matrix)
