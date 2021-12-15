#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix
import sys

HELP_INFO = [
    "Script is solving task 15 of advent of code 2021",
    "Arguments:",
    common.TAB + "input file"
]
arguments_keywords = ["inputFile"]

script_arguments = common.parse_arguments(arguments_keywords, HELP_INFO)
if script_arguments is None:
    exit(1)

input_file_name = script_arguments["inputFile"]
print("solving file: " + input_file_name)
input_lines = common.read_lines_from_file(input_file_name)


def pack_coordinates(x, y, matrix_size):
    return x * matrix_size + y


def unpack_coordinates(coordinates, matrix_size):
    return int(coordinates / matrix_size), coordinates % matrix_size


def find_lowest_risk_path(risk_matrix, x, y, parents, total_risk):
    size_x, size_y = common.get_matrix_size(risk_matrix)
    if x == size_x - 1 and y == size_y - 1:
        print(f"in {x}, {y}")

    # print(parents[x, y])
    parent_risk = total_risk.item(*parents[x, y])
    # print(parent_risk)
    if parent_risk + risk_matrix[x, y] > total_risk.item(x, y) > 0:
        return
    total_risk[x, y] = parent_risk + risk_matrix[x, y]
    # for next_x in range(max(0, x - 1), min(x + 1, size_x)):
    #     for next_y in range(max(0, y - 1), min(y + 1, size_y)):
    #         if x == next_x and y == next_y:
    #             continue
    nexts = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    for next_x, next_y in nexts:
        if not (0 <= next_x < size_x and 0 <= next_y < size_y):
            continue
        parents[next_x, next_y] = [x, y]
        find_lowest_risk_path(risk_matrix, next_x, next_y, parents, total_risk)
    return total_risk


def main():
    sys.setrecursionlimit(sys.getrecursionlimit() * 20)
    risk_matrix = numpy_matrix.get_matrix_from_string_lines(input_lines)
    parents = numpy.zeros_like(risk_matrix, tuple)
    parents[0, 0] = [0, 0]
    total_risk = numpy.zeros_like(risk_matrix)
    # print(parents)
    # print()
    # print(total_risk)
    # return
    result1 = find_lowest_risk_path(risk_matrix, 0, 0, parents, total_risk)
    result2 = 1

    print(f"task1: {result1}")
    print(f"task2: {result2}")


main()
