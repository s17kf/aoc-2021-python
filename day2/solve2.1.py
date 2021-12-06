#!/usr/bin/python3.10

import common

HELP_INFO = [
    "Script is solving task 1 for day 2 of advent of code 2021",
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
for line in inputLines:
    [command, val] = line.split()
    val = int(val)
    match command:
        case "forward":
            position += val
        case "down":
            depth += val
        case "up":
            depth -= val
            if(depth < 0):
                print("ERROR: depth is 0")
        case _:
            print("ERROR: unsupported command in line " + str(computedEntries + 1))
    computedEntries += 1

print("computed entries: " + str(computedEntries))
print("position: %d, depth: %d, multiplied: %d" % (position, depth, position * depth))
