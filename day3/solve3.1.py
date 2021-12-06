#!/usr/bin/python3.10

import common

HELP_INFO = [
    "Script is solving task 1 for day 3 of advent of code 2021",
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
    if zeros[i] > ones[i]:
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
