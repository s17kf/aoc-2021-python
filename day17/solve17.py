#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
import numpy
HELP_INFO = [
    "Script is solving task 17 of advent of code 2021",
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


def do_simulation_y(y_range, y_initial_step):
    y = i = y_max = 0
    y_v = y_initial_step
    while y > y_range[-1]:
        y += y_v
        y_v -= 1
        i += 1
        y_max = max(y, y_max)
    is_y_in_range = y_range[0] <= y <= y_range[-1]
    return is_y_in_range, y_max, i


def do_simulation_y_v2(y_range, y_initial_step):
    y = i = 0
    y_v = y_initial_step
    result = []
    while y >= y_range[0]:
        y += y_v
        y_v -= 1
        i += 1
        if y_range[0] <= y <= y_range[-1]:
            result.append((y_initial_step, i))
    return result


def do_simulation_x(x_range, x_initial_step, x_steps):
    x = 0
    x_v = x_initial_step
    for _ in range(x_steps):
        x_v = max(x_v - 1, 0)
        x += x_v
    return x_range[0] <= x <= x_range[-1]


def do_task1(y_range):
    for initial_step in range(1000):
        status, max_y, _ = do_simulation_y(y_range, initial_step)
        if status:
            result = (initial_step, max_y)
    return result


def do_task2(x_range, y_range):
    possible_y = []
    all_possible_initial_steps = []
    for initial_step in range(-200, 1500):
        new_y_initial_steps = do_simulation_y_v2(y_range, initial_step)
        for y in new_y_initial_steps:
            possible_y.append(y)
    for y, n in possible_y:
        for x_initial_step in range(100):
            if do_simulation_x(x_range, x_initial_step, n):
                all_possible_initial_steps.append(f"{x_initial_step}, {y}")
    return all_possible_initial_steps


def main():
    _, _, x_range, y_range = input_lines[0].split()
    x_range = [int(value) for value in x_range.strip("x=,").split("..")]
    y_range = [int(value) for value in y_range.strip("y=").split("..")]
    result1 = do_task1(y_range)
    result2 = do_task2(x_range, y_range)
    result2 = numpy.array(numpy.unique(result2))
    print(f"task1: {result1}")
    print(len(result2))


main()
