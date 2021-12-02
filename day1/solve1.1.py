#!/usr/bin/python3

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
increasing = 0
for i in range(1, len(inputLines)):
    currentLine = inputLines[i]
    previousLine = inputLines[i-1]
    if (int(currentLine) > int(previousLine)):
        increasing += 1
    computedEntries += 1

print("computed entries: " + str(computedEntries))
print("result: " + str(increasing))
