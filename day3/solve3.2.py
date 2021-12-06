#!/usr/bin/python3.10

import common

HELP_INFO = [
    "Script is solving task 2 for day 3 of advent of code 2021",
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


def get_one_item(lines, bit_for_gt, bit_for_other):
    i = 0
    lines_left = lines
    while not common.is_empty(lines_left):
        zeros = 0
        ones = 0
        lines = lines_left
        lines_left = []
        for line in lines:
            bit = line[i]
            if bit == "0":
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            chosen_bit = bit_for_gt
        else:
            chosen_bit = bit_for_other

        for line in lines:
            bit = line[i]
            if bit == chosen_bit:
                lines_left.append(line)
        if len(lines_left) == 1:
            return lines_left[0]
        i += 1


print("solving file: " + inputFileName)
inputLines = common.read_lines_from_file(inputFileName)

oxygenLeft = get_one_item(inputLines, "0", "1")
co2Left = get_one_item(inputLines, "1", "0")

oxygenStr = str(oxygenLeft)
co2Str = str(co2Left)

oxygen = int(oxygenStr, 2)
co2 = int(co2Str, 2)

print("oxygen: %s -> %d" % (oxygenStr, oxygen))
print("co2 %s -> %d" % (co2Str, co2))

print("%d * %d = %d" % (oxygen, co2, oxygen * co2))
