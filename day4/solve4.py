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

def getBoardItem(board, x, y):
    # x = int(x/5)
    # y = x + y
    return board[5*x+y]

boards = common.getListOfGroupsDividedEmptyLine(inputLines[2:])

def verifyItemsAtRow(board, x, y, numbers):
    for i in range(5):
        if not getBoardItem(board, x, i) in numbers:
            return False
    return True

def verifyItemsAtColumn(board, x, y, numbers):
    for i in range(5):
        if not getBoardItem(board, i, y) in numbers:
            return False
    return True


def verifyBoard(board, numbers):
    for num in numbers:
        for x in range(5):
            for y in range(5):
                print(x, y)
                if getBoardItem(board, x, y) == num:
                    if verifyItemsAtRow(board, x, y, numbers) or verifyItemsAtColumn(board, x, y, numbers):
                        return True
    return False

def getSumNumbersOnBoard(board, numbers):
    sum = 0
    for num in numbers:
        if num in boards:
            sum += num
    return sum

def doTask1(allNumbers, boards):
    currentNumbers = allNumbers[0:4]
    for i in range(4, len(allNumbers)):
        num = allNumbers[i]
        currentNumbers.append(num)
        # print(currentNumbers)
        for board in boards:
            if verifyBoard(board, currentNumbers):
                sumOfNums = getSumNumbersOnBoard(board, numbers)
                return sumOfNums, num

allNumbers = inputLines[0]
allNumbers = allNumbers.split(",")
allNumbers = [int(n) for n in allNumbers]
intBoards = []
for board in boards:
    board = board.split()
    board = [int(n) for n in board]
    intBoards.append(board)


print(doTask1(allNumbers, boards))

# print(allNumbers)
# for board in intBoards:
#     print(getBoardItem(board, 0, 0), getBoardItem(board, 0, 3),getBoardItem(board, 0,4),
#         getBoardItem(board,1,0),getBoardItem(board,1,2),getBoardItem(board,4,4))






print(f"task1: {0}")
print(f"task2: {1}")



