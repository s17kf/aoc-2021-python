#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix

HELP_INFO = [
    "Script is solving task 11 of advent of code 2021",
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


def flash(xx, yy, matrix, already_flashed):
    if already_flashed[xx, yy]:
        return
    size_x, size_y = numpy_matrix.size(matrix)
    start_x, end_x = max(0, xx - 1), min(size_x, xx + 2)
    start_y, end_y = max(0, yy - 1), min(size_y, yy + 2)
    already_flashed[xx, yy] = True
    points_to_flash = []
    for x, row in enumerate(matrix[start_x:end_x]):
        x += start_x
        for y, item in enumerate(row[start_y: end_y]):
            y += start_y
            if already_flashed[x, y]:
                continue
            matrix[x, y] += 1
            if matrix[x, y] > 9:
                points_to_flash.append(pack_coordinates(x, y, size_x))
    for point in points_to_flash:
        flash(*unpack_coordinates(point, size_x), matrix, already_flashed)


def step(matrix):
    size_x, size_y = numpy_matrix.size(matrix)
    for x, row in enumerate(matrix):
        for y, item in enumerate(row):
            matrix[x, y] += 1
    already_flashed = numpy.zeros((size_x, size_y), bool)
    for x, row in enumerate(matrix):
        for y, item in enumerate(row):
            if item > 9 and not already_flashed[x, y]:
                flash(x, y, matrix, already_flashed)
    flashes = 0
    for x, row in enumerate(matrix):
        for y, item in enumerate(row):
            if item > 9:
                flashes += 1
                matrix[x, y] = 0
    return flashes


def do_task1(lines, iterations=10):
    matrix = numpy_matrix.get_matrix_from_string_lines(lines)
    flashes = 0
    for i in range(iterations):
        flashes += step(matrix)
    return flashes


def do_task2(lines):
    matrix = numpy_matrix.get_matrix_from_string_lines(lines)
    iterations = 0
    while True:
        flashes = step(matrix)
        iterations += 1
        if flashes == matrix.size:
            return iterations


result1 = do_task1(input_lines, 100)
result2 = do_task2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
