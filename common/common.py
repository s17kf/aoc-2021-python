import sys

TAB = "    "

def isEmpty(array):
    return len(array) == 0

def getLastElement(array):
    return array[len(array) - 1]

def readLinesFromFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        file.close()
    return lines

def readScriptArguments(argumentKeywords):
    argumentToValueMap = {}
    if (len(sys.argv) != len(argumentKeywords) + 1):
        return argumentToValueMap
    for i in range(len(argumentKeywords)):
        argumentToValueMap[argumentKeywords[i]] = sys.argv[i+1]
    return argumentToValueMap

def printArrayLineByLine(array):
    for line in array:
        print(line)

def getListOfGroupsDividedEmptyLine(lines, delimiter = " "):
    groups = []
    lastGroup = ""

    for line in lines:
        if isEmpty(line):
            groups.append(lastGroup.lstrip())
            lastGroup = ""
            continue
        lastGroup += delimiter + line
    if lastGroup != "":
        groups.append(lastGroup.lstrip())
    return groups

def addOrIncreaseForKey(myDict, key, defaultValue = 1, valueToIncrease = 1):
    if key in myDict:
        myDict[key] += 1
    else:
        myDict[key] = defaultValue
    return myDict

