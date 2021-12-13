#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix

HELP_INFO = [
    "Script is solving task 13 of advent of code 2021",
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


def fold_y(paper, y):
    size_y, size_x = numpy_matrix.size(paper)
    up_size = y
    down_size = size_y - y - 1
    new_paper = numpy.zeros((max(up_size, down_size), size_x), int)
    for row_num in range(y - 1, -1, -1):
        new_paper[row_num] = paper[row_num]
    for row_num in range(y + 1, size_y):
        for x, _ in enumerate(paper[row_num]):
            new_paper[y - row_num, x] = paper[row_num, x] if paper[row_num, x] == 1 else \
                new_paper[y - row_num, x]
    return new_paper


def fold_x(paper, x):
    size_y, size_x = numpy_matrix.size(paper)
    left_size = x
    right_size = size_x - x - 1
    new_paper = numpy.zeros((size_y, max(left_size, right_size)), int)
    for column_num in range(x - 1, -1, -1):
        new_paper[:, column_num] = paper[:, column_num]
    for column_num in range(x + 1, size_x):
        for y, _ in enumerate(paper[:, column_num]):
            new_paper[y, x - column_num] = paper[y, column_num] if paper[y, column_num] == 1 else \
                new_paper[y, x - column_num]
    return new_paper


def generate_paper_and_folds_list(lines):
    dots, folds = common.get_list_of_groups_divided_empty_line(input_lines, ";")
    dots = dots.split(";")
    folds = folds.split(";")
    size_x = size_y = 0
    for dot in dots:
        dot_x, dot_y = int(dot.split(",")[0]), int(dot.split(",")[1])
        size_x = max(size_x, dot_x)
        size_y = max(size_y, dot_y)
    size_x += 1
    size_y += 1
    paper = numpy.zeros((size_y, size_x), int)
    for dot in dots:
        dot_x, dot_y = int(dot.split(",")[0]), int(dot.split(",")[1])
        paper[dot_y, dot_x] = 1

    return paper, folds


def do_task1(paper, folds):
    for fold in folds:
        fold_type, value = fold.split()[2].split("=")
        value = int(value)
        match fold_type:
            case "y":
                paper = fold_y(paper, value)
            case "x":
                paper = fold_x(paper, value)
        break
    return sum(sum(paper))


def do_task2(paper, folds):
    for fold in folds:
        fold_type, value = fold.split()[2].split("=")
        value = int(value)
        match fold_type:
            case "y":
                paper = fold_y(paper, value)
            case "x":
                paper = fold_x(paper, value)
    result = []
    for row in paper:
        result.append([item for item in row])
    return result


def main():
    paper, folds_list = generate_paper_and_folds_list(input_lines)
    result1 = do_task1(paper.copy(), folds_list.copy())
    result2 = do_task2(paper.copy(), folds_list.copy())

    print(f"task1: {result1}")
    print(f"task2:")
    common.print_array_line_by_line(result2)


main()
