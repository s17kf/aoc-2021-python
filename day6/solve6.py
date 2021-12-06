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

dayToFishCount = {}
dayToBabyFishCount = {}

for daysLeft in daysLeftList:
    common.addOrIncreaseForKey(dayToFishCount, daysLeft)

print(dayToFishCount)
fishes = len(daysLeftList)

def handleBabyFishesForDayInPeriod(day, dayToFishCount, dayToBabyFishCount, fishes):#, oneDayToAdult, twoDaysToAdult, fishes):
    # twoDaysToAdult = dayToFishCount[day]
    # common.addOrIncreaseForKey(dayToFishCount, (day+2)%period, oneDayToAdult, oneDayToAdult)
    # common.addOrIncreaseForKey(dayToBabyFishCount, (day+2)%period, twoDaysToAdult, twoDaysToAdult)
    if day in dayToFishCount:
        dayToBabyFishCount[(day + 2) % period] = dayToFishCount[day]
        fishes += dayToFishCount[day]
    # oneDayToAdult = twoDaysToAdult
    # twoDaysToAdult = dayToFishCount[day]
    # fishes += twoDaysToAdult
    return fishes #, oneDayToAdult, twoDaysToAdult

def growUpBabyFishesForDayInPeriod(day, dayToFishCount, dayToBabyFishCount, fishes):#, oneDayToAdult, twoDaysToAdult, fishes):
    if day in dayToBabyFishCount:
        common.addOrIncreaseForKey(dayToFishCount, day, dayToBabyFishCount[day], dayToBabyFishCount[day])
        del dayToBabyFishCount[day]

def countAllFishes(dayToFishCount, dayToBabyFishCount):
    count = 0
    for key in dayToFishCount:
        count += dayToFishCount[key]
    for key in dayToBabyFishCount:
        count += dayToBabyFishCount[key]
    return count

twoDaysToAdult = 0
oneDayToAdult = 0

for i in range(daysToSymulate + 1):
    dayOfPeriod = i % period
    # if dayOfPeriod in dayToFishCount or oneDayToAdult > 0:
    #     # fishes, oneDayToAdult, twoDaysToAdult = handleBabyFishesForDayInPeriod(dayOfPeriod, dayToFishCount, oneDayToAdult, twoDaysToAdult, fishes)
    #     fishes = handleBabyFishesForDayInPeriod(dayOfPeriod, dayToFishCount, dayToBabyFishCount, fishes)
    fishes = handleBabyFishesForDayInPeriod(dayOfPeriod, dayToFishCount, dayToBabyFishCount, fishes)
    growUpBabyFishesForDayInPeriod((dayOfPeriod-1)%period, dayToFishCount, dayToBabyFishCount, fishes)
    # else:
    #     oneDayToAdult = twoDaysToAdult
    #     twoDaysToAdult = 0    
    # print(f"{i+1}: {fishes} {twoDaysToAdult} {oneDayToAdult}")
    tmpFishes = countAllFishes(dayToFishCount, dayToBabyFishCount)
    print(f"{i+1}: {tmpFishes}: {len(dayToFishCount)}: {dayToFishCount} {len(dayToBabyFishCount)}:{dayToBabyFishCount}")

# for day in range (1, daysToSymulate+1):
#     for i in range(len(daysLeftList)):
#         daysLeft = daysLeftList[i]
#         if daysLeft == 0:
#             daysLeftList.append(initialTimer)
#         daysLeft = daysLeft - 1 if daysLeft >= period else (daysLeft - 1) % period
#         daysLeftList[i] = daysLeft
    # print(f"{len(daysLeftList)}: {daysLeftList}")

# result = 0
# for key in dayToFishCount:
#     result += dayToFishCount[key]

# result += oneDayToAdult
# result += twoDaysToAdult

result = countAllFishes(dayToFishCount, dayToBabyFishCount)

# for i in range(-7, 8):
#     print(f"{i} % 7 = {i%7}")


result1 = len(daysLeftList)

print(f"task1: {fishes}")
print(f"task2: {result}")



