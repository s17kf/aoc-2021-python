#!/usr/bin/python3.10

import common
import math

HELP_INFO = [
    "Script is solving task 9 of advent of code 2021",
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


def is_lower_than_adjacent(matrix, xx, yy):
    size_x, size_y = common.get_matrix_size(matrix)
    start_x = max(xx - 1, 0)
    start_y = max(yy - 1, 0)
    current_item = matrix[xx][yy]
    for x, row in enumerate(matrix[start_x:xx + 2]):
        x += start_x
        if x < 0 or x > size_x:
            continue
        for y, item in enumerate(row[start_y:yy + 2]):
            y += start_y
            if y < 0 or y > size_y:
                continue
            if x == xx and y == yy:
                continue
            if x != xx and y != yy:
                continue
            if int(item) <= int(current_item):
                return False
    return True


def do_task1(lines):
    matrix = common.get_matrix_from_string_lines(lines)
    lower_than_adjacent = []
    for x, row in enumerate(matrix):
        for y, item in enumerate(row):
            if is_lower_than_adjacent(matrix.copy(), x, y):
                lower_than_adjacent.append(1 + int(item))
    return sum(lower_than_adjacent)


def pack_coordinates(x, y, matrix_size):
    return x * matrix_size + y


def unpack_coordinates(coordinates, matrix_size):
    return int(coordinates / matrix_size), coordinates % matrix_size


def get_basin(coordinates, matrix, basin):
    size_x, size_y = common.get_matrix_size(matrix)
    x, y = unpack_coordinates(coordinates, size_y)
    if x > 0 and matrix[x - 1][y] > matrix[x][y] and matrix[x - 1][y] != 9 \
            and pack_coordinates(x - 1, y, size_y) not in basin:
        point = pack_coordinates(x - 1, y, size_y)
        basin.append(point)
        basin = get_basin(point, matrix, basin)
    if x < size_x - 1 and matrix[x + 1][y] > matrix[x][y] and matrix[x + 1][y] != 9 \
            and pack_coordinates(x + 1, y, size_y) not in basin:
        point = pack_coordinates(x + 1, y, size_y)
        basin.append(point)
        basin = get_basin(point, matrix, basin)
    if y > 0 and matrix[x][y - 1] > matrix[x][y] and matrix[x][y - 1] != 9 \
            and pack_coordinates(x, y - 1, size_y) not in basin:
        point = pack_coordinates(x, y - 1, size_y)
        basin.append(point)
        basin = get_basin(point, matrix, basin)
    if y < size_y - 1 and matrix[x][y + 1] > matrix[x][y] and matrix[x][y + 1] != 9 \
            and pack_coordinates(x, y + 1, size_y) not in basin:
        point = pack_coordinates(x, y + 1, size_y)
        basin.append(point)
        basin = get_basin(point, matrix, basin)
    return basin


def do_task2(lines):
    matrix = common.get_matrix_from_string_lines(lines, common.return_int_arg)
    size_x, size_y = common.get_matrix_size(matrix)
    lowest_points_coordinates = []
    for x, row in enumerate(matrix):
        for y, item in enumerate(row):
            if is_lower_than_adjacent(matrix.copy(), x, y):
                lowest_points_coordinates.append(pack_coordinates(x, y, size_y))
    basins = []
    for point in lowest_points_coordinates:
        basins.append(get_basin(point, matrix, [point]))
    basins_sizes = [len(basin) for basin in basins]
    return basins_sizes


result1 = do_task1(input_lines)
result2 = do_task2(input_lines)

result2 = sorted(result2)[len(result2)-3:]
print(result2)

print(f"task1: {result1}")
print(f"task2: {math.prod(result2)}")
