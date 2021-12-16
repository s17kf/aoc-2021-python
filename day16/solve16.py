#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix

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


def remove_first_n_bits(bin_data, n):
    for i in range(n):
        if len(bin_data) == 0:
            return
        bin_data.pop(0)


def pop_packet_version_and_type_id(bin_data):
    version = int(''.join(bin_data[:3]), 2)
    type_id = int(''.join(bin_data[3:6]), 2)
    for _ in range(6):
        bin_data.pop(0)
    return version, type_id


def get_packet_version_and_type_id(bin_data):
    version = int(''.join(bin_data[:3]), 2)
    type_id = int(''.join(bin_data[3:6]), 2)
    return version, type_id


def pop_zeros_at_beginning(bin_data):
    while len(bin_data) > 0 and bin_data[0] == '0':
        bin_data.pop(0)


def pop_trailing_zeros(bin_data):
    while len(bin_data) > 0 and bin_data[-1] == '0':
        bin_data.pop()


def pop_literal_packet(bin_data):
    data = ""
    first_bit_in_group = 1
    while first_bit_in_group != '0':
        first_bit_in_group = bin_data.pop(0)
        group = bin_data[:4]
        data += ''.join(group)
        remove_first_n_bits(bin_data, 4)
    # print(f"literal: {data}")
    return data

def get_literal_packet(bin_data):
    data = ""
    first_bit_in_group = 1
    position = 0
    while first_bit_in_group != '0':
        first_bit_in_group = bin_data[0]
        group = bin_data[1:5]
        data += ''.join(group)
    # print(f"literal: {data}")
    return data


def get_subpackets(bin_data):
    length_type_bit = bin_data.pop(0)
    if length_type_bit == '0':
        length_of_subpackets_length = 15
        subpackets_length = int(''.join(bin_data[:length_of_subpackets_length]), 2)
        remove_first_n_bits(bin_data, length_of_subpackets_length)
        subpackets_bits = bin_data[:subpackets_length]
        remove_first_n_bits(bin_data, subpackets_length)
        return subpackets_bits
    else:
        length_of_subpackets_count = 11
        subpackets_count = int(''.join(bin_data[:length_of_subpackets_count]), 2)
        remove_first_n_bits(bin_data, length_of_subpackets_count)
        bin_data_copy = bin_data.copy()
        subpackets_bits = []
        for _ in range(subpackets_count):
            version, type_id = pop_packet_version_and_type_id(bin_data_copy)
            if type_id == 4:
                subpackets_bits.append(bin_data[:6 + get_literal_packet(bin_data_copy) + 1])
                remove_first_n_bits(bin_data, 6 + get_literal_packet(bin_data_copy))
            else:
                subpackets_bits.append(bin_data[:6 + 1 + len(get_subpackets(bin_data_copy)) + 1])
                remove_first_n_bits(bin_data, 6 + 1 + len(get_subpackets(bin_data_copy)))
        # remove_first_n_bits(bin_data, len(subpackets_bits))
        return subpackets_bits


def calculate_value(version, type_id, bin_data, versions):
    calculated_values = []
    if type_id == 4:
        calculated_values.append(int(pop_literal_packet(bin_data)))
    else:
        subpackets_bits_list = get_subpackets(bin_data)
        print(subpackets_bits_list)


def get_transmition_value(data, is_hex=True):
    binary_data = data
    if is_hex:
        binary_data = ""
        for hex in data:
            binary_data += format(int(hex, 16), '04b')
    print(binary_data)
    binary_data = [bit for bit in binary_data]
    if is_hex:
        pop_trailing_zeros(binary_data)
    versions = []
    # while len(binary_data) > 0:
    version, type_id = pop_packet_version_and_type_id(binary_data)
    versions.append(version)
    if type_id == 4:
        return int(pop_literal_packet(binary_data), 2)
    else:
        return calculate_value(version, type_id, binary_data, versions)



result1 = 0
result2 = get_transmition_value(input_lines[0])

print(f"task1: {sum([int(version) for version in result1])} {result1}")
print(f"task2: {result2}")
