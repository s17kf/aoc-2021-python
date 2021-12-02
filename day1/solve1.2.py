#!/usr/bin/python3

import common

isEmpty = common.isEmpty

HELP_INFO = [
"Script is solving task 2 for day 1 of advent of code 2021",
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
for i in range(3, len(inputLines)):
    line0 = int(inputLines[i-3])
    line1 = int(inputLines[i-2])
    line2 = int(inputLines[i-1])
    line3 = int(inputLines[i-0])
    sum1 = line0 + line1 + line2
    sum2 = line1 + line2 + line3
    if (sum2 > sum1):
        increasing += 1
    computedEntries += 1

print("computed entries: " + str(computedEntries))
print("result: " + str(increasing))
