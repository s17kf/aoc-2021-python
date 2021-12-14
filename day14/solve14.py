#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from collections import Counter

HELP_INFO = [
    "Script is solving task 14 of advent of code 2021",
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


def do_task1(lines, iterations=10):
    polymer, rules = common.get_list_of_groups_divided_empty_line(lines, ";")
    rules = {rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in rules.split(";")}
    for i in range(iterations):
        new_polymer = polymer[0]
        for prev_pos, char in enumerate(polymer[1:]):
            pair = polymer[prev_pos] + char
            new_polymer += rules[pair] + char
        polymer = new_polymer
        letter_counter = Counter(polymer)
    return common.get_last_element(sorted(letter_counter.values())) - \
        sorted(letter_counter.values())[0]


def do_task2(lines, iterations=40):
    polymer, rules = common.get_list_of_groups_divided_empty_line(lines, ";")
    rules = {rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in rules.split(";")}
    pairs_counter = Counter()
    for i, char in enumerate(polymer[1:]):
        pairs_counter[polymer[i] + char] += 1

    for i in range(iterations):
        new_pairs_counter = Counter()
        for pair in pairs_counter:
            new_pair1 = pair[0] + rules[pair]
            new_pair2 = rules[pair] + pair[1]
            new_pairs_counter[new_pair1] += pairs_counter[pair]
            new_pairs_counter[new_pair2] += pairs_counter[pair]
        pairs_counter = new_pairs_counter

    letters_counter = Counter()
    for pair in pairs_counter:
        for char in pair:
            letters_counter[char] += pairs_counter[pair]
    for char, count in letters_counter.items():
        letters_counter[char] = (count + 1) // 2 \
            if char in [polymer[0], polymer[-1]] else count // 2

    return common.get_last_element(sorted(letters_counter.values())) - \
        sorted(letters_counter.values())[0]


result1 = do_task1(input_lines)
print(f"task1: {result1}")

result2 = do_task2(input_lines, 40)
print(f"task2: {result2}")
