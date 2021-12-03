#!/usr/bin/python3.10

import common
import codecs

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

computedEntries = 0
zeros = []
ones = []
gammaStr = ""
epsStr = ""

for bit in inputLines[0]:
    zeros.append(0)
    ones.append(0)

for line in inputLines:
    for i in range(len(line)):
        bit = line[i]
        if bit == "0":
            zeros[i] += 1
        else:
            ones[i] += 1

    computedEntries += 1

print(zeros)
print(ones)

for i in range(len(zeros)):
    if(zeros[i] > ones[i]):
        gammaStr += "0"
        epsStr += "1"
    else:
        gammaStr += "1"
        epsStr += "0"

print("computed entries: " + str(computedEntries))

print(gammaStr)
print(epsStr)

gamma = int(gammaStr, 2)
eps = int(epsStr, 2)

print("%d * %d = %d" % (gamma, eps, gamma * eps))
