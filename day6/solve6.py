#!/usr/bin/python3.10

import common

isEmpty = common.isEmpty

HELP_INFO = [
"Script is solving tasks for day 6 of advent of code 2021",
"Arguments:",
common.TAB + "input file",
common.TAB + "number of days to simulate"
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

daysToSymulate = int(scriptArguments["daysToSymulate"])

dayToFishCount = [0,0,0,0,0,0,0]
dayToBabyFishCount = [0,0,0,0,0,0,0]

for daysLeft in daysLeftList:
    dayToFishCount[daysLeft] += 1

print(dayToFishCount)

def generateBabyFishesForDayInPeriod(day, dayToFishCount, dayToBabyFishCount):
    dayToBabyFishCount[(day + 2) % period] = dayToFishCount[day % period]
    return dayToFishCount, dayToBabyFishCount

def growUpBabyFishesForDayInPeriod(day, dayToFishCount, dayToBabyFishCount):
    growUpDay = (day -1) % period
    dayToFishCount[growUpDay] += dayToBabyFishCount[growUpDay]
    dayToBabyFishCount[growUpDay] = 0
    return dayToFishCount, dayToBabyFishCount

for day in range(daysToSymulate):
    dayToFishCount, dayToBabyFishCount = generateBabyFishesForDayInPeriod(day, dayToFishCount, dayToBabyFishCount)
    dayToFishCount, dayToBabyFishCount = growUpBabyFishesForDayInPeriod(day, dayToFishCount, dayToBabyFishCount)

result = sum(dayToFishCount) + sum(dayToBabyFishCount)
print(f"result: {result}")
