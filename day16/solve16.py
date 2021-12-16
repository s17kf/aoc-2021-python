#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""
import sys

import common
import numpy

OPERATIONS = {
    0: lambda a: sum(a),
    1: lambda a: numpy.prod(a),
    2: lambda a: min(a),
    3: lambda a: max(a),
    4: "literal",
    5: lambda a: int(a[0] > a[1]),
    6: lambda a: int(a[0] < a[1]),
    7: lambda a: int(a[0] == a[1])
}


def remove_first_n_bits(bin_data, n):
    popped_bits = bin_data[:n]
    for i in range(n):
        bin_data.pop(0)
    return popped_bits


def pop_packet_version_and_type_id(bin_data):
    version = int(''.join(bin_data[:3]), 2)
    type_id = int(''.join(bin_data[3:6]), 2)
    for _ in range(6):
        bin_data.pop(0)
    return version, type_id


def pop_literal_packet(bin_data):
    data = ""
    first_bit_in_group = 1
    while first_bit_in_group != '0':
        first_bit_in_group = bin_data.pop(0)
        group = bin_data[:4]
        data += ''.join(group)
        remove_first_n_bits(bin_data, 4)
    return data


def calculate_value(bin_data, versions, values):
    version, type_id = pop_packet_version_and_type_id(bin_data)
    versions.append(version)
    if type_id == 4:
        result = int(pop_literal_packet(bin_data), 2)
        values.append(result)
    else:
        length_type_id = bin_data.pop(0)
        if length_type_id == '0':
            length = int(''.join(remove_first_n_bits(bin_data, 15)), 2)
            subpacket = remove_first_n_bits(bin_data, length)
            result = OPERATIONS[type_id](calculate_value_type0(subpacket, versions))
            values.append(result)
        else:
            packets_count = int(''.join(remove_first_n_bits(bin_data, 11)), 2)
            result = OPERATIONS[type_id](calculate_value_type1(bin_data, packets_count, versions))
            values.append(result)
    return versions, result


def calculate_value_type0(bin_data, versions):
    values = []
    while len(bin_data) > 0:
        calculate_value(bin_data, versions, values)
    return values


def calculate_value_type1(bin_data, packets, versions):
    values = []
    for _ in range(packets):
        calculate_value(bin_data, versions, values)
    return values


def solve_packet(data):
    bin_data = ""
    for hex_digit in data:
        bin_data += format(int(hex_digit, 16), '04b')
    bin_data = [bit for bit in bin_data]
    return calculate_value(bin_data, [], [])


print(sys.argv)

HELP_INFO = [
    "Script is solving task 16 of advent of code 2021",
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

result1, result2 = solve_packet(input_lines[0])
print()
print(f"task1: {sum(result1)} <-- {result1}")
print(f"task2: {result2}")
