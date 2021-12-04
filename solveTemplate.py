#!/usr/bin/python3.10

import common

isEmpty = common.isEmpty

HELP_INFO = [
"Script is solving task 1 for day 3 of advent of code 2021",
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










print(f"task1: {0}")
print(f"task2: {1}")



