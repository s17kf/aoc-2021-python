#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix

HELP_INFO = [
    "Script is solving task 19 of advent of code 2021",
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

SIN = [0, 1, 0, -1, 0]
COS = [1, 0, -1, 0, 1]


def get_coordinates_plus_offset(line):
    x, y, z = line.split(",")
    return int(x), int(y), int(z)


def turn(coords, n, axis):
    x, y, z = coords
    sin = SIN[n]
    cos = COS[n]
    match axis:
        case 'x':
            return x, cos * y + sin * z, cos * z - sin * y
        case 'y':
            return cos * x + sin * z, y, cos * z - sin * x
        case 'z':
            return cos * x + sin * y, cos * y - sin * x, z


def turn_scanner_data(scanner_data, n, axis):
    for i, data in enumerate(scanner_data):
        scanner_data[i] = turn(data, n, axis)


def count_common(scanner1_data, scanner2_data, offset):
    offset_x, offset_y, offset_z = offset
    common_beacons = 0
    for x, y, z in scanner2_data:
        if (x + offset_x, y + offset_y, z + offset_z) in scanner1_data:
            common_beacons += 1
    return common_beacons


def get_offset_if_12_common(scanner1_data, scanner_2_data):
    for x1, y1, z1 in scanner1_data:
        for x2, y2, z2 in scanner_2_data:
            offset = x1 - x2, y1 - y2, z1 - z2
            if count_common(scanner1_data, scanner_2_data, offset) >= 12:
                return True, offset
    return False, None


def has_12_common_beacons(scanner1_data, scanner2_data):
    scanner2_data_copy = scanner2_data.copy()
    for x in range(4):
        turn_scanner_data(scanner2_data_copy, 1, 'x')
        for y in range(4):
            turn_scanner_data(scanner2_data_copy, 1, 'y')
            for z in range(4):
                turn_scanner_data(scanner2_data_copy, 1, 'z')
                is_12_common, offset = get_offset_if_12_common(scanner1_data, scanner2_data_copy)
                if is_12_common:
                    turn_scanner_data(scanner2_data, x + 1, 'x')
                    turn_scanner_data(scanner2_data, y + 1, 'y')
                    turn_scanner_data(scanner2_data, z + 1, 'z')
                    offset_x, offset_y, offset_z = offset
                    for i, (xx, yy, zz) in enumerate(scanner2_data):
                        scanner2_data[i] = xx + offset_x, yy + offset_y, zz + offset_z

                    return True, offset
    return False, None


def print_scanner_data(scanner_data):
    for data in scanner_data:
        print(data)


def do_task1(lines):
    input_by_scanners = common.get_list_of_groups_divided_empty_line(lines, delimiter=";")
    input_by_scanners = [data.split(";")[1:] for data in input_by_scanners]

    all_scanners_data = []
    for scanner_input in input_by_scanners:
        scanner_data = []
        for data in scanner_input:
            scanner_data.append(get_coordinates_plus_offset(data))
        all_scanners_data.append(scanner_data)

    common_scanners = {}
    last_identified = {0: (0, (0, 0, 0))}
    scanners_positions = {0: (0, 0, 0)}
    while len(common_scanners) < len(all_scanners_data):
        scanners_to_compare = list(last_identified)
        for key in last_identified:
            offset_to, (x, y, z) = last_identified[key]
            offset_to_x, offset_to_y, offset_to_z = scanners_positions[offset_to]
            scanners_positions[key] = offset_to_x + x, offset_to_y + y, offset_to_z + z
            common_scanners[key] = last_identified[key]
        last_identified.clear()

        print(len(common_scanners), common_scanners)
        print(scanners_to_compare)
        for i in range(len(all_scanners_data)):
            if i in common_scanners or i in scanners_to_compare:
                continue
            print(i)
            for scanner_to_compare in scanners_to_compare:
                has_12_common, offset = has_12_common_beacons(all_scanners_data[scanner_to_compare],
                                                              all_scanners_data[i])
                if has_12_common:
                    last_identified[i] = (scanner_to_compare, offset)
                    break
        print(f" last_identifed: {len(last_identified)}, {last_identified}")
    all_beacons_size = sum([len(scanner_data) for scanner_data in all_scanners_data])
    all_beacons = []
    for scanner_data in all_scanners_data:
        for coords in scanner_data:
            coords = [str(c) for c in coords]
            all_beacons.append(','.join(coords))
    print(all_beacons_size)
    print(len(all_beacons))
    unique_beacons = numpy.array(all_beacons)
    scanners_positions = {}
    for key, (_, coords) in common_scanners.items():
        scanners_positions[key] = coords
    return numpy.unique(unique_beacons).size, scanners_positions


def do_task2(scanners_positions):
    max_distance = 0
    for key1, coords1 in scanners_positions.items():
        for key2, coords2 in scanners_positions.items():
            if key1 == key2:
                continue
            distance = sum(abs(c1 - c2) for c1, c2 in zip(coords1, coords2))
            if distance > max_distance:
                max_distance, scanner1, scanner2 = distance, key1, key2
    return max_distance, scanner1, scanner2


result1, positions = do_task1(input_lines)
result2 = do_task2(positions)

print(f"task1: {result1}")
print(f"task2: {result2}")
