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


def find_lowest_risk_path(risk_matrix, parents, total_risk, nexts):
    if common.is_empty(nexts):
        print("nexts empty")
        return total_risk
    size_x, size_y = common.get_matrix_size(risk_matrix)
    print("dupa")
    x, y, parent_x, parent_y = nexts.pop(0)
    print(x, y, parent_x, parent_y)
    # if x == size_x - 1 and y == size_y - 1:
    # print(f"in {x}, {y}")
    # print(parents[x, y])
    parent_risk = total_risk[parent_x, parent_y]
    # print(parent_risk)
    if parent_risk + risk_matrix[x, y] > total_risk[x, y]:
        return find_lowest_risk_path(risk_matrix, parents, total_risk, nexts)
    total_risk[x, y] = parent_risk + risk_matrix[x, y]
    parents[x, y] = [parent_x, parent_y]
    # for next_x in range(max(0, x - 1), min(x + 1, size_x)):
    #     for next_y in range(max(0, y - 1), min(y + 1, size_y)):
    #         if x == next_x and y == next_y:
    #             continue
    for new_next in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
        if not (0 <= new_next[0] < size_x and 0 <= new_next[1] < size_y):
            continue
        new_next.append(x)
        new_next.append(y)
        if total_risk[x, y] + risk_matrix[new_next[0], new_next[1]] < total_risk[
            new_next[0], new_next[1]]:
            nexts.insert(0, new_next)
    # for next_x, next_y in nexts:
    #     if not (0 <= next_x < size_x and 0 <= next_y < size_y):
    #         continue
    #     parents[next_x, next_y] = [x, y]
    return find_lowest_risk_path(risk_matrix, parents, total_risk, nexts)
    # return total_risk


def find_lowest_risk_path_iterative(risk_matrix, parents, total_risk, nexts):
    size_x, size_y = common.get_matrix_size(risk_matrix)
    while len(nexts) > 0:
        x, y, parent_x, parent_y = nexts.pop(0)
        # print(x, y, parent_x, parent_y)
        parent_risk = total_risk[parent_x, parent_y]
        # print(parent_risk)
        if parent_risk + risk_matrix[x, y] > total_risk[x, y]:
            continue
        total_risk[x, y] = parent_risk + risk_matrix[x, y]
        parents[x, y] = [parent_x, parent_y]
        for new_next in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            if not (0 <= new_next[0] < size_x and 0 <= new_next[1] < size_y):
                continue
            new_next.append(x)
            new_next.append(y)
            if total_risk[x, y] + risk_matrix[new_next[0], new_next[1]] < total_risk[
                new_next[0], new_next[1]]:
                nexts.insert(0, new_next.copy())
        # return find_lowest_risk_path(risk_matrix, parents, total_risk, nexts)
    return total_risk


def copy_into_full_matrix_incremented_by(full_matrix, input_matrix, offset_x, offset_y,
                                         increment_value):
    for x, row in enumerate(input_matrix):
        for y, item in enumerate(row):
            full_matrix[y + offset_y, x + offset_x] = (input_matrix[y, x] + increment_value) % 10


def get_full_risk_matrix(input_risk_matrix):
    size_multiplier = 5
    org_size_x, org_size_y = common.get_matrix_size(input_risk_matrix)
    size_x = org_size_x * size_multiplier
    size_y = org_size_y * size_multiplier
    real_risk_matrix = numpy.zeros((size_x, size_y), int)
    for x in range(size_multiplier):
        for y in range(size_multiplier):
            copy_into_full_matrix_incremented_by(real_risk_matrix, input_risk_matrix,
                                                 x * org_size_x,
                                                 y * org_size_y, x + y)
    return real_risk_matrix


def main():
    # numpy.set_printoptions(threshold=sys.maxsize)
    # sys.setrecursionlimit(sys.getrecursionlimit() * 20)
    risk_matrix = numpy_matrix.get_matrix_from_string_lines(input_lines)
    # risk_matrix = get_full_risk_matrix(risk_matrix)
    print(risk_matrix)
    parents = numpy.zeros_like(risk_matrix, tuple)
    parents[0, 0] = [0, 0]
    total_risk = numpy.full_like(risk_matrix, 500)
    total_risk[0, 0] = 0
    # print(parents)
    # print()
    # print(total_risk)
    # return
    result1 = find_lowest_risk_path_iterative(risk_matrix, parents, total_risk,
                                              [[0, 1, 0, 0], [1, 0, 0, 0]])
    result2 = 1

    print(f"task1: {result1}")
    print(f"task2: {result2}")


main()
