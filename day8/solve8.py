#!/usr/bin/python3.10

import common
from enum import Enum, auto
from collections import Counter

HELP_INFO = [
    "Script is solving task 8 of advent of code 2021",
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

SEGMENTS = "abcdefg"

def do_task1(lines):
    segments_count_to_digit = {2: 1, 3: 7, 4: 4, 7: 8}
    digits_counter = Counter()
    for line in lines:
        digits = line.split(" | ")[1].split()
        for digit in digits:
            size = len(digit)
            if size not in segments_count_to_digit:
                continue
            digits_counter[segments_count_to_digit[size]] += 1
    return digits_counter.total()


def find_pattern_of_6_and_9_and_0(patterns, digit_to_pattern, pattern_to_digit):
    pattern_of_1 = digit_to_pattern[1]
    pattern_of_4 = digit_to_pattern[4]
    for pattern in patterns:
        size = len(pattern)
        if size != 6:
            continue
        digit = None
        for seg in pattern_of_1:
            if seg not in pattern:
                digit = 6
                break
        if digit is None:
            digit = 9
            for seg in pattern_of_4:
                if seg not in pattern:
                    digit = 0
        digit_to_pattern[digit] = pattern
        pattern_to_digit[pattern] = digit


def find_pattern_of_5(patterns, digit_to_pattern, pattern_to_digit):
    pattern_of_6 = digit_to_pattern[6]
    segment_not_in_6 = [seg for seg in SEGMENTS if seg not in pattern_of_6][0]
    for pattern in patterns:
        if len(pattern) != 5 or segment_not_in_6 in pattern:
            continue
        digit_to_pattern[5] = pattern
        pattern_to_digit[pattern] = 5


def find_pattern_of_2_and_3(patterns, digit_to_pattern, pattern_to_digit):
    pattern_of_1 = digit_to_pattern[1]
    for pattern in patterns:
        if pattern in pattern_to_digit:
            continue
        if len(pattern) != 5:
            continue
        digit = 3
        for seg in pattern_of_1:
            if seg not in pattern:
                digit = 2
                break
        digit_to_pattern[digit] = pattern
        pattern_to_digit[pattern] = digit


def find_numbers(patterns):
    segments_count_to_unique_digit = {2: 1, 3: 7, 4: 4, 7: 8}
    digit_to_pattern = {}
    pattern_to_digit = {}
    for pattern in patterns:
        size = len(pattern)
        if size not in segments_count_to_unique_digit:
            continue
        digit_to_pattern[segments_count_to_unique_digit[size]] = pattern
        pattern_to_digit[pattern] = segments_count_to_unique_digit[size]
    find_pattern_of_6_and_9_and_0(patterns, digit_to_pattern, pattern_to_digit)
    find_pattern_of_5(patterns, digit_to_pattern, pattern_to_digit)
    find_pattern_of_2_and_3(patterns, digit_to_pattern, pattern_to_digit)
    print(f"{len(digit_to_pattern)}: {digit_to_pattern}")
    return pattern_to_digit

def do_task2(lines):
    segments_count_to_digit = {2: 1, 3: 7, 4: 4, 7: 8}
    # digits_counter = Counter()
    sum = 0
    for line in lines:
        patterns, digits = line.split(" | ")
        # patterns = [sorted(segs) for segs in patterns.split()]
        # digits = [sorted(segs) for segs in digits.split()]
        patterns = [''.join(sorted(segs)) for segs in patterns.split()]
        digits = [''.join(sorted(segs)) for segs in digits.split()]
        # patterns = patterns.split()
        # digits = digits.split()
        pattern_to_digit = find_numbers(patterns)
        # sorted_pattern_to_digit = {}
        # for pattern in pattern_to_digit:
        #     sorted_pattern_to_digit[]
        number = ""
        for pattern in digits:
            # digits_counter[pattern_to_digit[pattern]] += 1
            number += str(pattern_to_digit[pattern])
        sum += int(number)
    return sum


result1 = do_task1(input_lines)
result2 = do_task2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
