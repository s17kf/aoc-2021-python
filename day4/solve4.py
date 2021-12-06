#!/usr/bin/python3.10

import common

HELP_INFO = [
    "Script is solving task 1 for day 4 of advent of code 2021",
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


def get_board_item(board, x, y):
    # x = int(x/5)
    # y = x + y
    return board[5*x+y]


def verify_items_at_row(board, row, numbers):
    for i in range(5):
        if not get_board_item(board, row, i) in numbers:
            # print(f"{getBoardItem(board, row, i)} not in {numbers}")
            return False
    return True


def verify_items_at_column(board, column, numbers):
    for i in range(5):
        if not get_board_item(board, i, column) in numbers:
            return False
    return True


def verify_board(board, numbers):
    for i in range(5):
        if verify_items_at_row(board, i, numbers) or verify_items_at_column(board, i, numbers):
            return True
    return False


def get_sum_numbers_on_board(board, numbers):
    count = 0
    for num in board:
        if not num in numbers:
            # print(f"{num} not in {board}")
            count += num
    return count


def do_task1(all_numbers, boards):
    current_numbers = all_numbers[0:4]
    for i in range(4, len(all_numbers)):
        num = all_numbers[i]
        current_numbers.append(num)
        for board in boards:
            if verify_board(board, current_numbers):
                sum_of_nums = get_sum_numbers_on_board(board, current_numbers)
                return sum_of_nums, num


def do_task2(all_numbers, boards):
    current_numbers = all_numbers[0:4]
    for i in range(4, len(all_numbers)):
        num = all_numbers[i]
        current_numbers.append(num)
        for board in boards:
            if verify_board(board, current_numbers):
                boards.remove(board)
                if common.is_empty(boards):
                    sum_of_nums = get_sum_numbers_on_board(board, current_numbers)
                    return sum_of_nums, num


def main():
    boards = common.get_list_of_groups_divided_empty_line(inputLines[2:])
    all_numbers = inputLines[0]
    all_numbers = all_numbers.split(",")
    all_numbers = [int(n) for n in all_numbers]
    int_boards = []
    for board in boards:
        board = board.split()
        board = [int(n) for n in board]
        int_boards.append(board)

    sum_of_nums, num = do_task1(all_numbers, int_boards)
    result1 = sum_of_nums * num
    sum_of_nums2, num2 = do_task2(all_numbers, int_boards)
    result2 = sum_of_nums2 * num2

    print(f"task1: {sum_of_nums} * {num} = {result1}")
    print(f"task2: {sum_of_nums2} * {num2} = {result2}")


main()
