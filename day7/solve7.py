#!/usr/bin/python3.10

import common

HELP_INFO = [
    "Script is solving task 7 of advent of code 2021",
    "Arguments:",
    common.TAB + "input file"
]
arguments_keywords = ["inputFile"]

script_arguments = common.parse_arguments(arguments_keywords, HELP_INFO)
if script_arguments is None:
    exit(1)

input_file_name = script_arguments["inputFile"]
print("solving file: " + input_file_name)
input_lines = common.read_lines_from_file(input_file_name)


def get_median(list_of_elements):
    list_of_elements.sort()
    size = len(list_of_elements)
    if size % 2 == 1:
        return list_of_elements[int(size / 2)]
    else:
        return_idx_first = int(size/2) - 1
        return (list_of_elements[return_idx_first] + list_of_elements[return_idx_first + 1]) / 2


def get_cost2(source, dest):
    distance = abs(source - dest)
    cost = 0
    for i in range(1, distance+1):
        cost += i
    return cost


def do_task(positions):
    print(len(positions))
    positions = [int(pos) for pos in positions.split(",")]
    average = sum(positions) / len(positions)
    median = get_median(positions.copy())
    need_fuel = 0
    need_fuel2 = 9999999999999
    print(f"average: {average}")
    average = int(round(average))
    median = int(median)
    print(average)
    print(f"{median}, {average}")
    need_fuel2 = 0
    for pos in positions:
        need_fuel += abs(median - pos)
        need_fuel2 += get_cost2(pos,average)

    # for dest in range(max(positions) + 1):
    #     need_fuel2_tmp = 0
    #     for pos in positions:
    #         need_fuel2_tmp += get_cost2(pos, dest)
    #     if need_fuel2_tmp < need_fuel2:
    #         need_fuel2 = need_fuel2_tmp
    return int(need_fuel), need_fuel2


result1, result2 = do_task(input_lines[0])

print(f"task1: {result1}")
print(f"task2: {result2}")
