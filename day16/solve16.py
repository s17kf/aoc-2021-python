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


def pop_zeros_at_beginning(bin_data):
    while len(bin_data) > 0 and bin_data[0] == '0':
        bin_data.pop(0)


def pop_literal_packet(bin_data):
    data = ""
    first_bit_in_group = 1
    while first_bit_in_group != '0':
        first_bit_in_group = bin_data.pop(0)
        group = bin_data[:4]
        data += ''.join(group)
        remove_first_n_bits(bin_data, 4)
    pop_zeros_at_beginning(bin_data)
    return data


def pop_subpackets(bin_data, versions, subpackets):
    length_type_bit = bin_data.pop(0)
    if length_type_bit == '0':
        length_of_subpackets_length = 15
        # print(bin_data[:length_of_subpackets_length])
        subpackets_length = int(''.join(bin_data[:length_of_subpackets_length]), 2)
        for _ in range(length_of_subpackets_length):
            bin_data.pop(0)
        subpackets.append(''.join(bin_data[:subpackets_length]))
        print(f"{subpackets_length} vs {len(subpackets[-1])} ... left {len(bin_data)}")
        remove_first_n_bits(bin_data, subpackets_length)
        # pop_zeros_at_beginning(bin_data)
        return

    length_of_subpackets_count = 11
    subpackets_count = int(''.join(bin_data[:length_of_subpackets_count]), 2)
    remove_first_n_bits(bin_data, length_of_subpackets_count)
    # while bin_data[0] == '0':
    #     bin_data.pop(0)
    # subpackets = []
    print(f"subpackets_count: {subpackets_count}")
    for _ in range(subpackets_count):
        version, type_id = pop_packet_version_and_type_id(bin_data)
        versions.append(version)
        print(version, type_id)
        if type_id != 4:
            pop_subpackets(bin_data, versions, subpackets)
        else:
            literal_packet = pop_literal_packet(bin_data)
    pop_zeros_at_beginning(bin_data)
    return


def get_versions(data, is_hex=True):
    binary_data = data
    if is_hex:
        binary_data = ""
        for hex in data:
            binary_data += format(int(hex, 16), '04b')
    # print(binary_data)
    binary_data = [bit for bit in binary_data]
    # print(pop_packet_version_and_type_id(binary_data))
    parsed = False
    versions = []
    subpackets = []
    while len(binary_data) > 0:
        # print(binary_data)
        version, type_id = pop_packet_version_and_type_id(binary_data)
        versions.append(version)
        print(version, type_id)
        if type_id != 4:
            pop_subpackets(binary_data, versions, subpackets)
        else:
            literal_packet = pop_literal_packet(binary_data)
            # subpackets.append(literal_packet)
            # version, type_id = pop_packet_version_and_type_id(binary_data)
            # versions.append(version)
            # print(int(literal_packet, 2))
            break

    print(subpackets)
    for subpacket in subpackets:
        print(subpacket)
        versions += (get_versions(subpacket, False))

    return versions
    # return ''.join(binary_data)


result1 = get_versions(input_lines[0])
result2 = 1

print(f"task1: {result1}")
print(f"task2: {result2}")
