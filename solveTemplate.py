#!/usr/bin/python3.10

import common

HELP_INFO = [
    "Script is solving task DAY_NUM of advent of code 2021",
    "Arguments:",
    common.TAB + "input file"
]
arguments_keywords = ["inputFile"]

script_arguments = common.parse_arguments(arguments_keywords, HELP_INFO)
if script_arguments is None:
    exit(1)

inputFileName = script_arguments["inputFile"]
print("solving file: " + inputFileName)
inputLines = common.read_lines_from_file(inputFileName)








result1 = 0
result2 = 1

print(f"task1: {result1}")
print(f"task2: {result2}")
