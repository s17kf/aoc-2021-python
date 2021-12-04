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

def verifyItemsAtRow(board, row, numbers):
    for i in range(5):
        if not getBoardItem(board, row, i) in numbers:
            # print(f"{getBoardItem(board, row, i)} not in {numbers}")
            return False
    return True

def verifyItemsAtColumn(board, column, numbers):
    for i in range(5):
        if not getBoardItem(board, i, column) in numbers:
            return False
    return True


def verifyBoard(board, numbers):
    # if len(numbers) == 7:
        # print(numbers)
        # print(board)
    for i in range(5):
        if verifyItemsAtRow(board, i, numbers) or verifyItemsAtColumn(board, i, numbers):
            return True
    return False

def getSumNumbersOnBoard(board, numbers):
    sum = 0
    for num in board:
        if not num in numbers:
            # print(f"{num} not in {board}")
            sum += num
    return sum


def doTask1(allNumbers, boards):
    lastIndex = 0
    currentNumbers = allNumbers[0:4]
    for i in range(4, len(allNumbers)):
        num = allNumbers[i]
        currentNumbers.append(num)
        # print(currentNumbers)
        for board in boards:
            if verifyBoard(board, currentNumbers):
                # print(currentNumbers)
                sumOfNums = getSumNumbersOnBoard(board, currentNumbers)
                return sumOfNums, num

def doTask2(allNumbers, boards):
    lastIndex = 0
    lastWinner = None
    currentNumbers = allNumbers[0:4]
    for i in range(4, len(allNumbers)):
        num = allNumbers[i]
        currentNumbers.append(num)
        # print(currentNumbers)
        for board in boards:
            if verifyBoard(board, currentNumbers):
                # print(currentNumbers)
                lastWinner = board
                boards.remove(board)
                if isEmpty(boards):
                    sumOfNums = getSumNumbersOnBoard(board, currentNumbers)
                    return sumOfNums, num



allNumbers = inputLines[0]
allNumbers = allNumbers.split(",")
allNumbers = [int(n) for n in allNumbers]
intBoards = []
for board in boards:
    board = board.split()
    board = [int(n) for n in board]
    intBoards.append(board)

sumOfNums, num = doTask1(allNumbers, intBoards)
result1 = sumOfNums * num
sumOfNums2, num2 = doTask2(allNumbers, intBoards)
result2 = sumOfNums2 * num2

# print(allNumbers)
# for board in intBoards:
#     print(getBoardItem(board, 0, 0), getBoardItem(board, 0, 3),getBoardItem(board, 0,4),
#         getBoardItem(board,1,0),getBoardItem(board,1,2),getBoardItem(board,4,4))






print(f"task1: {sumOfNums} * {num} = {result1}")
print(f"task2: {sumOfNums2} * {num2} = {result2}")



