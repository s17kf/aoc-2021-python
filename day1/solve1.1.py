#!/usr/bin/python3

import common

HELP_INFO = [
    "Script is solving task 1 for day 1 of advent of code 2021",
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

computedEntries = 0
increasing = 0
for i in range(1, len(inputLines)):
    currentLine = inputLines[i]
    previousLine = inputLines[i-1]
    if int(currentLine) > int(previousLine):
        increasing += 1
    computedEntries += 1

print("computed entries: " + str(computedEntries))
print("result: " + str(increasing))
