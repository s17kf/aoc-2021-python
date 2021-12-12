import numpy
import common


def get_matrix_from_string_lines(lines, typ=int, parse_function=common.return_int_arg):
    matrix = numpy.zeros((len(lines), len(lines[0])), typ)
    for i, line in enumerate(lines):
        matrix[i] = ([parse_function(char) for char in line])
        matrix[i] = ([parse_function(char) for char in line])
    return matrix


def size(matrix):
    return len(matrix), len(matrix[0])
