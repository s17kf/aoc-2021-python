#!/usr/bin/python3.10

import common

isEmpty = common.isEmpty

HELP_INFO = [
"Script is solving task 1 for day 1 of advent of code 2021",
"Arguments:",
common.TAB + "input file"
]

argumentsKeywords = ["inputFile"]

scriptArguments = common.readScriptArguments(argumentsKeywords)

if (isEmpty(scriptArguments)):
    common.printArrayLineByLine(HELP_INFO)
    exit(1)

inputFileName = scriptArguments["inputFile"]

print("solving file: " + inputFileName)
inputLines = common.readLinesFromFile(inputFileName)

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
