#!/usr/bin/python3.10

import common
from collections import Counter

is_empty = common.is_empty

HELP_INFO = [
    "Script is solving tasks for day 6 of advent of code 2021",
    "Arguments:",
    common.TAB + "input file",
    common.TAB + "number of days to simulate"
]
arguments_keywords = ["inputFile", "daysToSimulate"]

script_arguments = common.parse_arguments(arguments_keywords, HELP_INFO)
if script_arguments is None:
    exit(1)

inputFileName = script_arguments["inputFile"]
daysToSimulate = int(script_arguments["daysToSimulate"])

PERIOD = 7
DAYS_TO_GROWUP = 2


def generate_baby_fishes_for_day_in_period(day, day_to_fish_counter, day_to_baby_fish_counter):
    day_to_baby_fish_counter[(day + DAYS_TO_GROWUP) % PERIOD] = day_to_fish_counter[day % PERIOD]


def grow_up_baby_fishes_for_day_in_period(day, day_to_fish_counter, day_to_baby_fish_counter):
    grow_up_day = (day - 1) % PERIOD
    day_to_fish_counter[grow_up_day] += day_to_baby_fish_counter[grow_up_day]
    day_to_baby_fish_counter[grow_up_day] = 0


def main():
    print("solving file: " + inputFileName)
    input_lines = common.read_lines_from_file(inputFileName)

    days_left_list = [int(days) for days in input_lines[0].split(",")]

    day_to_fish_counter = Counter(days_left_list)
    day_to_baby_fish_counter = Counter()

    for day in range(daysToSimulate):
        generate_baby_fishes_for_day_in_period(day, day_to_fish_counter, day_to_baby_fish_counter)
        grow_up_baby_fishes_for_day_in_period(day, day_to_fish_counter, day_to_baby_fish_counter)

    result = day_to_fish_counter.total() + day_to_baby_fish_counter.total()
    print(f"result: {result}")


main()
