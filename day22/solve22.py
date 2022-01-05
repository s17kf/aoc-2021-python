#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix

HELP_INFO = [
    "Script is solving task 22 of advent of code 2021",
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


def get_ranges(input_ranges):
    rx, ry, rz = [r.lstrip("xyz=").split("..") for r in input_ranges.split(",")]
    # rx = [int(r) for r in rx]
    # ry = [int(r) for r in ry]
    # rz = [int(r) for r in rz]
    rx = int(rx[0]), int(rx[1])
    ry = int(ry[0]), int(ry[1])
    rz = int(rz[0]), int(rz[1])
    return rx, ry, rz


def set_value(cubes, value, ranges, size, grid_range):
    offset = size // 2
    rx, ry, rz = ranges
    for z in range(max(rz[0], grid_range[0]), min(rz[-1] + 1, grid_range[1] + 1)):
        for y in range(max(ry[0], grid_range[0]), min(ry[-1] + 1, grid_range[1] + 1)):
            for x in range(max(rx[0], grid_range[0]), min(rx[-1] + 1, grid_range[1] + 1)):
                cubes[z + offset, y + offset, x + offset] = value


def do_task1(lines, size):
    cubes = numpy.zeros((size, size, size), int)
    command_values = {"on": 1, "off": 0}
    for i, line in enumerate(lines):
        # print(i)
        command, ranges = line.split()
        ranges = get_ranges(ranges)
        set_value(cubes, command_values[command], ranges, size, (-50, 50))
        # print(f"{command_values[command]}: {ranges}")
    return sum(sum(sum(cubes)))


def turn_off_cuboids(on_cuboids, ranges):
    rx, ry, rz = ranges
    rx_begin, rx_end = rx
    ry_begin, ry_end = ry
    rz_begin, rz_end = rz
    for i, cuboid in enumerate(on_cuboids):
        crx, cry, crz = cuboid
        crx_begin, crx_end = crx
        cry_begin, cry_end = cry
        crz_begin, crz_end = crz
        if rx_begin <= crx_begin <= rx_end or rx_begin <= crx_end <= rx_end and \
                ry_begin <= cry_begin <= ry_end or ry_begin <= cry_end <= ry_end and \
                rz_begin <= crz_begin <= rz_end or rz_begin <= crz_end <= rz_end:
            pass


def do_task2(lines):
    command_values = {"on": 1, "off": 0}
    on_cuboids = []
    for i, line in enumerate(lines):
        # print(i)
        command, ranges = line.split()
        ranges = get_ranges(ranges)
        if command == "on":
            on_cuboids.append(ranges)

    # print('\n'.join([','.join(cuboid) for cuboid in on_cuboids]))
    # print(f"{len(on_cuboids)}: {on_cuboids}")


result1 = do_task1(input_lines, 101)
print(f"task1: {result1}")

result2 = do_task2(input_lines)
print(f"task2: {result2}")
