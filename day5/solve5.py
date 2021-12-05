#!/usr/bin/python3.10

import common
from enum import Enum, auto

isEmpty = common.isEmpty

HELP_INFO = [
"Script is solving tasks for day 5 of advent of code 2021",
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

class LineType(Enum):
    horizontal = auto()
    vertical = auto()
    other = auto()

def getCoordinatesPair(line):
    return line.split(" -> ")

def getXY(coords):
    x, y = coords.split(",")
    return int(x), int(y)

def findMaxCoordinate(lines):
    maximum = 0
    for line in inputLines:
        x1, y1 = getXY(getCoordinatesPair(line)[0])
        x2, y2 = getXY(getCoordinatesPair(line)[1])
        coordsInLine = [x1, y1, x2, y2]
        largest = max(coordsInLine)
        maximum = largest if largest > maximum else maximum
    return maximum

def getLineType(c1, c2):
    x1, y1 = getXY(c1)
    x2, y2 = getXY(c2)
    if x1 == x2:
        return LineType.vertical
    if y1 == y2:
        return LineType.horizontal
    return LineType.other

def prepareMatrix(lines):
    areaSize = findMaxCoordinate(lines) + 1
    matrix = [[0 for x in range(areaSize)] for y in range(areaSize)]
    return matrix

def handleHorizontalLine(matrix, c1, c2):
    x1, y1 = getXY(c1)
    x2, y2 = getXY(c2)
    if x2 < x1:
        x1, x2 = x2, x1
    for x in range(x1, x2+1):
        matrix[y1][x] += 1

def handleVerticalLine(matrix, c1, c2):
    x1, y1 = getXY(c1)
    x2, y2 = getXY(c2)
    if y2 < y1:
        y1, y2 = y2, y1
    for y in range(y1, y2+1):
        matrix[y][x1] += 1

def handleDiagonalLine(matrix, c1, c2):
    x1, y1 = getXY(c1)
    x2, y2 = getXY(c2)
    x = x1
    y = y1
    while x != x2:
        matrix[y][x] += 1
        x = x + 1 if x1 < x2 else x - 1
        y = y + 1 if y1 < y2 else y - 1 
    matrix[y][x] += 1

def nopFun(matrix, c1, c2):
    pass

def doTask(lines, handleDiagonalLineFun = nopFun):
    matrix = prepareMatrix(lines)
    for line in lines:
        c1, c2 = getCoordinatesPair(line)
        lineType = getLineType(c1, c2)
        match lineType:
            case LineType.horizontal:
                handleHorizontalLine(matrix, c1, c2)
            case LineType.vertical:
                handleVerticalLine(matrix, c1, c2)
            case LineType.other:
                handleDiagonalLineFun(matrix, c1, c2)
    result = 0
    for row in matrix:
        for v in row:
            if v > 1:
                result += 1
    return result


result1 = doTask(inputLines)
result2 = doTask(inputLines, handleDiagonalLine)

print()
print(f"task1: {result1}")
print(f"task2: {result2}")
