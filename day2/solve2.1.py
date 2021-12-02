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
