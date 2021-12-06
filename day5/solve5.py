#!/usr/bin/python3.10

import common
from enum import Enum, auto

HELP_INFO = [
    "Script is solving task 1 for day 5 of advent of code 2021",
    "Arguments:",
    common.TAB + "input file"
]
arguments_keywords = ["inputFile"]

script_arguments = common.parse_arguments(arguments_keywords, HELP_INFO)
if script_arguments is None:
    exit(1)

inputFileName = script_arguments["inputFile"]
print("solving file: " + inputFileName)
inputLines = common.read_lines_from_file(inputFileName)


class LineType(Enum):
    horizontal = auto()
    vertical = auto()
    other = auto()


def get_coordinates_pair(line):
    return line.split(" -> ")


def get_xy(coords):
    x, y = coords.split(",")
    return int(x), int(y)


def find_max_coordinate(lines):
    maximum = 0
    for line in inputLines:
        x1, y1 = get_xy(get_coordinates_pair(line)[0])
        x2, y2 = get_xy(get_coordinates_pair(line)[1])
        coordsInLine = [x1, y1, x2, y2]
        largest = max(coordsInLine)
        maximum = largest if largest > maximum else maximum
    return maximum


def get_line_type(c1, c2):
    x1, y1 = get_xy(c1)
    x2, y2 = get_xy(c2)
    if x1 == x2:
        return LineType.vertical
    if y1 == y2:
        return LineType.horizontal
    return LineType.other


def prepare_matrix(lines):
    area_size = find_max_coordinate(lines) + 1
    matrix = [[0 for x in range(area_size)] for y in range(area_size)]
    return matrix


def handle_horizontal_line(matrix, c1, c2):
    x1, y1 = get_xy(c1)
    x2, y2 = get_xy(c2)
    if x2 < x1:
        x1, x2 = x2, x1
    for x in range(x1, x2 + 1):
        matrix[y1][x] += 1


def handle_vertical_line(matrix, c1, c2):
    x1, y1 = get_xy(c1)
    x2, y2 = get_xy(c2)
    if y2 < y1:
        y1, y2 = y2, y1
    for y in range(y1, y2 + 1):
        matrix[y][x1] += 1


def handle_diagonal_line(matrix, c1, c2):
    x1, y1 = get_xy(c1)
    x2, y2 = get_xy(c2)
    x = x1
    y = y1
    while x != x2:
        matrix[y][x] += 1
        x = x + 1 if x1 < x2 else x - 1
        y = y + 1 if y1 < y2 else y - 1
    matrix[y][x] += 1


def nop_fun(*args):
    pass


def do_task(lines, handle_diagonal_line_fun=nop_fun):
    matrix = prepare_matrix(lines)
    for line in lines:
        c1, c2 = get_coordinates_pair(line)
        line_type = get_line_type(c1, c2)
        match line_type:
            case LineType.horizontal:
                handle_horizontal_line(matrix, c1, c2)
            case LineType.vertical:
                handle_vertical_line(matrix, c1, c2)
            case LineType.other:
                handle_diagonal_line_fun(matrix, c1, c2)
    result = 0
    for row in matrix:
        for v in row:
            if v > 1:
                result += 1
    return result


result1 = do_task(inputLines)
result2 = do_task(inputLines, handle_diagonal_line)

print()
print(f"task1: {result1}")
print(f"task2: {result2}")
