#!/usr/bin/python3.10

import common

isEmpty = common.isEmpty

HELP_INFO = [
"Script is solving tasks for day 6 of advent of code 2021",
"Arguments:",
common.TAB + "input file"
]

argumentsKeywords = ["inputFile", "daysToSymulate"]

scriptArguments = common.readScriptArguments(argumentsKeywords)

if (isEmpty(scriptArguments)):
    common.printArrayLineByLine(HELP_INFO)
    exit(1)

inputFileName = scriptArguments["inputFile"]

print("solving file: " + inputFileName)
inputLines = common.readLinesFromFile(inputFileName)

period = 7
initialTimer = 8

daysLeftList = [int(days) for days in inputLines[0].split(",")]

print(daysLeftList)

# daysToSymulate = 80
daysToSymulate = int(scriptArguments["daysToSymulate"])

for day in range (1, daysToSymulate+1):
    for i in range(len(daysLeftList)):
        daysLeft = daysLeftList[i]
        if daysLeft == 0:
            daysLeftList.append(initialTimer)
        daysLeft = daysLeft - 1 if daysLeft >= period else (daysLeft - 1) % period
        daysLeftList[i] = daysLeft
    # print(f"{len(daysLeftList)}: {daysLeftList}")


# for i in range(-7, 8):
#     print(f"{i} % 7 = {i%7}")


result1 = len(daysLeftList)

print(f"task1: {result1}")
print(f"task2: {1}")



