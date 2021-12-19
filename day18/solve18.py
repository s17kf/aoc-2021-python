#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
import math
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix

HELP_INFO = [
    "Script is solving task 18 of advent of code 2021",
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


def explode(number_to_explode, left_num_index, right_num_index):
    left_side_parens = 0
    # print(left_num_index, right_num_index, number_to_explode)
    for index in range(left_num_index - 1, 0, -1):
        if number_to_explode[index] in ['[', ']', ',']:
            if number_to_explode[index] == '[':
                # print()
                left_side_parens += 1
            continue
        number_to_explode[index] = str(
            int(number_to_explode[index]) + int(number_to_explode[left_num_index]))
        break

    right_side_parens = 0
    for index in range(right_num_index + 1, len(number_to_explode)):
        if number_to_explode[index] in ['[', ']', ',']:
            if number_to_explode[index] == ']':
                right_side_parens += 1
            continue
        # print(number_to_explode[index], number_to_explode[right_num_index])
        number_to_explode[index] = str(
            int(number_to_explode[index]) + int(number_to_explode[right_num_index]))
        break

    if right_side_parens == 1:
        for _ in range(3):
            number_to_explode.pop(right_num_index)
    else:
        number_to_explode.pop(right_num_index + 1)
        # number_to_explode.pop(right_num_index)
        number_to_explode[right_num_index] = '0'

    if left_side_parens == 1:
        for _ in range(3):
            number_to_explode.pop((left_num_index - 2))
    else:
        number_to_explode[left_num_index] = '0'
        # number_to_explode.pop(left_num_index+1)
        number_to_explode.pop(left_num_index - 1)

    # print(''.join(number_to_explode))


def explode_if_should_exploded(number_to_explode: list[str]) -> bool:
    opened_indices = []
    current_deep = 0
    for i, char in enumerate(number_to_explode):
        # print(f"{i}: {char}")
        match char:
            case '[':
                opened_indices.append(i)
                # current_deep += 1
            case ']':
                # print(i, char, number_to_explode)
                opened_indices.pop()
                # current_deep -= 1
            case ',':
                continue
            case _:
                if len(opened_indices) == 5:
                    explode(number_to_explode, i, i + 2)
                    return True
    return False


def split_if_should_split(number_to_explode):
    for i, char in enumerate(number_to_explode):
        if char in ['[', ']', ',']:
            continue
        if int(char) < 10:
            continue
        number_to_explode.pop(i)
        n1 = math.floor(int(char) / 2)
        n2 = math.ceil(int(char) / 2)
        number_to_explode.insert(i, ']')
        number_to_explode.insert(i, str(n2))
        number_to_explode.insert(i, ',')
        number_to_explode.insert(i, str(n1))
        number_to_explode.insert(i, '[')
        return True
    return False


def reduce_number(number_to_reduce):
    if explode_if_should_exploded(number_to_reduce):
        # print("explode")
        return True
    # print("not exploded")
    # print(''.join(number_to_reduce))
    return split_if_should_split(number_to_reduce)


def add_numbers(n1, n2):
    return "[" + n1 + "," + n2 + "]"


def calculate_magnitude(number):
    number_size = len(number)
    number = [char for char in number]
    for i, n in enumerate(number):
        if '0' <= n <= '9':
            number[i] = int(n)
    while number[0] == '[':
        for i, element in enumerate(number):
            # print(element)
            if i + 2 >= len(number) or not (
                    isinstance(element, int) and isinstance(number[i + 2], int)):
                continue
            # if number[i + 1] != ',':
            #     continue
            # print(i, number)
            n1 = element
            n2 = number[i + 2]
            # print(n1, n2)
            for _ in range(5):
                number.pop(i - 1)
            number.insert(i - 1, 3 * n1 + 2 * n2)
    return number


def do_task1(lines):
    numbers_count = len(lines)
    for i in range(numbers_count - 1):
        n1 = lines.pop(0)
        n2 = lines.pop(0)
        number = add_numbers(n1, n2)
        # print(number)
        number = [char for char in number]
        while reduce_number(number):
            pass
        # lines.insert(0, number)
        number = ''.join(number)
        lines.insert(0, number)
    return calculate_magnitude(lines[0])


def do_task2(lines):
    max_magnitude = 0
    numbers_count = len(lines)
    for index1, n1 in enumerate(lines):
        # print(lines)
        # print()
        for index2, n2, in enumerate(lines):
            if index1 == index2:
                continue
            number = add_numbers(n1, n2)
            number = [char for char in number]
            while reduce_number(number):
                pass
            number = ''.join(number)
            magintuda = calculate_magnitude(number)[0]
            max_magnitude = max(int(max_magnitude), int(magintuda))
    return max_magnitude


result1 = do_task1(input_lines.copy())
print(f"task1: {result1}")

result2 = do_task2(input_lines.copy())
print(f"task2: {result2}")
