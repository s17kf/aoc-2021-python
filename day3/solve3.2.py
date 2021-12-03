#!/usr/bin/python3.10

import common

isEmpty = common.isEmpty

HELP_INFO = [
"Script is solving task 2 for day 3 of advent of code 2021",
"Arguments:",
common.TAB + "input file"
]

argumentsKeywords = ["inputFile"]

scriptArguments = common.readScriptArguments(argumentsKeywords)

def getOneItem(lines, bitForGt, bitForOther):
    i = 0
    linesLeft = lines
    while not isEmpty(linesLeft):
        zeros = 0
        ones = 0
        lines = linesLeft
        linesLeft = []
        for line in lines:
            bit = line[i]
            if bit == "0":
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            chosenBit = bitForGt
        else:
            chosenBit = bitForOther

        for line in lines:
            bit = line[i]
            if bit == chosenBit:
                linesLeft.append(line)
        if len(linesLeft) == 1:
            return linesLeft[0]
        i += 1

if (isEmpty(scriptArguments)):
    common.printArrayLineByLine(HELP_INFO)
    exit(1)

inputFileName = scriptArguments["inputFile"]

print("solving file: " + inputFileName)
inputLines = common.readLinesFromFile(inputFileName)

oxygenLeft = getOneItem(inputLines, "0", "1")
co2Left = getOneItem(inputLines, "1", "0")

oxygenStr = str(oxygenLeft)
co2Str = str(co2Left)

oxygen = int(oxygenStr, 2)
co2 = int(co2Str, 2)

print("oxygen: %s -> %d" % (oxygenStr, oxygen))
print("co2 %s -> %d" % (co2Str, co2))

print("%d * %d = %d" % (oxygen, co2, oxygen * co2))
