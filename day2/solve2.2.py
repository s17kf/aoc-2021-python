#!/usr/bin/python3.10

import common

is_empty = common.is_empty

HELP_INFO = [
    "Script is solving task 2 for day 2 of advent of code 2021",
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
position = 0
depth = 0
aim = 0
for line in inputLines:
    [command, x] = line.split()
    x = int(x)
    match command:
        case "forward":
            position += x
            depth += aim * x
        case "down":
            aim += x
        case "up":
            aim -= x
        case _:
            print("ERROR: unsupported command in line " + str(computedEntries + 1))
    computedEntries += 1

print("computed entries: " + str(computedEntries))
print("position: %d, depth: %d, multiplied: %d" % (position, depth, position * depth))
