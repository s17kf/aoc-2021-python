#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
import numpy
from common import numpy_matrix
import bisect

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


def find_lowest_risk_path(risk_matrix, total_risk):
    size_x, size_y = common.get_matrix_size(risk_matrix)
    nexts = [[0, 0, 0]]

    while len(nexts) > 0:
        risk, x, y = nexts.pop(0)
        for new_next in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            if not (0 <= new_next[0] < size_x and 0 <= new_next[1] < size_y):
                continue
            potential_new_next_risk = total_risk[x, y] + risk_matrix[new_next[0], new_next[1]]
            if potential_new_next_risk< total_risk[new_next[0], new_next[1]]:
                new_next.insert(0, potential_new_next_risk)
                if total_risk.item(*new_next[1:]) != MAX_VALUE:
                    i = bisect.bisect_left(nexts, new_next)
                    nexts.pop(i)
                total_risk[new_next[1], new_next[2]] = potential_new_next_risk
                i = bisect.bisect_left(nexts, new_next)
                nexts.insert(i, new_next)
    return total_risk


def copy_into_full_matrix_incremented_by(full_matrix, input_matrix, offset_x, offset_y,
                                         increment_value):
    for y, row in enumerate(input_matrix):
        for x, item in enumerate(row):
            value = input_matrix[y, x] + increment_value
            full_matrix[y + offset_y, x + offset_x] = value if value <= 9 else value % 10 + 1


def get_full_risk_matrix(input_risk_matrix):
    size_multiplier = 5
    org_size_x, org_size_y = common.get_matrix_size(input_risk_matrix)
    size_x = org_size_x * size_multiplier
    size_y = org_size_y * size_multiplier
    real_risk_matrix = numpy.zeros((size_x, size_y), int)
    for y in range(size_multiplier):
        for x in range(size_multiplier):
            copy_into_full_matrix_incremented_by(real_risk_matrix, input_risk_matrix,
                                                 x * org_size_x,
                                                 y * org_size_y, x + y)
    return real_risk_matrix


MAX_VALUE = 500000000


def main():
    risk_matrix = numpy_matrix.get_matrix_from_string_lines(input_lines)
    total_risk = numpy.full_like(risk_matrix, MAX_VALUE)
    total_risk[0, 0] = 0

    result1 = find_lowest_risk_path(risk_matrix, total_risk)
    print(f"task1: {result1}")

    risk_matrix = get_full_risk_matrix(risk_matrix)
    total_risk = numpy.full_like(risk_matrix, MAX_VALUE)
    total_risk[0, 0] = 0

    result2 = find_lowest_risk_path(risk_matrix, total_risk)
    print()
    print(f"task2: {result2}")


main()
