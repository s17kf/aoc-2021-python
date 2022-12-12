#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix
import math

HELP_INFO = [
    "Script is solving task 24 of advent of code 2021",
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

OPERATIONS = {
    "inp": "input",  # lambda args: args[0],
    "add": lambda args: sum(args),
    "mul": lambda args: math.prod(args),
    "div": lambda args: args[0] // args[1],
    "mod": lambda args: args[0] % args[1],
    "eql": lambda args: int(args[0] == args[1])
}


def check_model_number(input, instructions):
    current_input_pointer = 0
    variables = {
        # 'w': 0,
        # 'x': 0,
        # 'y': 0,
        # 'z': 0
        'w': '0',
        'x': '0',
        'y': '0',
        'z': '0'
    }
    for instruction in instructions:
        inst, args = instruction.split(" ", 1)
        args = [arg for arg in args.split()]
        result_variable = args[0]
        args = [variables.get(arg, arg) for arg in args]
        if inst == "inp":
            variables[result_variable] = input[current_input_pointer]
            current_input_pointer += 1
        else:
            # variables[result_variable] = OPERATIONS[inst](args)
            variables[result_variable] = str(OPERATIONS[inst]([int(arg) for arg in args]))

    print(variables)
    return variables['z']


def find_biggest_valid_model_number(instructions):
    hipotetical_model_number = 99999999999999 + 1
    # hipotetical_model_number = 99999999915535 + 1
    # hipotetical_model_number = 13579246899999 + 1
    hipotetical_model_number = 11111111111110 + 1
    # 99999691895167 11111381612744


    while True:
        hipotetical_model_number += 1
        if '0' in str(hipotetical_model_number):
            continue
        print(hipotetical_model_number)
        if check_model_number(str(hipotetical_model_number), instructions) == '0':
            return hipotetical_model_number

result1 = find_biggest_valid_model_number(input_lines)
result2 = 1

print(f"task1: {result1}")
print(f"task2: {result2}")
