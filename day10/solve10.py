#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from enum import Enum, auto
from collections import Counter
import numpy

HELP_INFO = [
    "Script is solving task DAY_NUM of advent of code 2021",
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

OPENING_BRACKETS = {"(": 3, "[": 57, "{": 1197, "<": 25137}
CLOSING_BRACKETS = {")": 3, "]": 57, "}": 1197, ">": 25137}

OPENING_BRACKETS2 = {"(": 1, "[": 2, "{": 3, "<": 4}
CLOSING_BRACKETS2 = {")": 1, "]": 2, "}": 3, ">": 4}


def score_corrupted_line(line):
    open_brackets = []
    for bracket in line:
        if bracket in OPENING_BRACKETS:
            open_brackets.append(bracket)
        elif common.is_empty(open_brackets):
            continue
        elif OPENING_BRACKETS[common.get_last_element(open_brackets)] == CLOSING_BRACKETS[bracket]:
            open_brackets.pop()
        else:
            return CLOSING_BRACKETS[bracket]
    return 0


def get_missing_brackets(incomplete_line):
    open_brackets = []
    for bracket in incomplete_line:
        if bracket in OPENING_BRACKETS2:
            open_brackets.append(bracket)
        else:
            open_brackets.pop()
    return reversed(open_brackets)


def score_missing_brackets(missing_brackets):
    score = 0
    for bracket in missing_brackets:
        score = score * 5 + OPENING_BRACKETS2[bracket]
    return score


def score_corrupted_lines(lines):
    return [score_corrupted_line(line) for line in lines]


def find_incomplete_lines_scores(lines):
    missing_brackets_scores = [score_missing_brackets(get_missing_brackets(line)) for line in lines
                               if score_corrupted_line(line) == 0]
    return sorted(missing_brackets_scores)[int(len(missing_brackets_scores) / 2)]


result1 = sum(score_corrupted_lines(input_lines))
result2 = find_incomplete_lines_scores(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
