#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from enum import Enum, auto
from collections import Counter
import numpy
from common import numpy_matrix

HELP_INFO = [
    "Script is solving task 21 of advent of code 2021",
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

PLAYERS_COUNT = 2
POSITIONS_ON_BOARD = 10


def move(position, last_dice, all_positions):
    last_dice = (last_dice + 3)
    # position += 3 * last_dice
    # while position > all_positions:
    #     overlaps = position // all_positions
    #     position = position % all_positions + overlaps
    position = (position + 3 * last_dice) % all_positions
    if position == 0:
        position = 10
    return position, last_dice


def do_task1(positions, win_score, positions_on_board):
    scores = [0 for _ in positions]
    last_dice = -1
    current_player = 0
    players_count = len(positions)
    while all([score < win_score for score in scores]):
        positions[current_player], last_dice = move(
            positions[current_player], last_dice, positions_on_board)
        scores[current_player] += positions[current_player]
        current_player = (current_player + 1) % players_count
        # print(positions, last_dice, scores)
    return scores, last_dice + 1, scores[current_player] * (last_dice + 1)


# def move_v2(positions, positions_count, all_positions):
#     dice_sums = Counter()
#     for i in range(3):

def get_possible_v2_moves_sum_step(dice, dices_sum, moves_left, end_sums):
    dices_sum += dice
    if moves_left == 0:
        end_sums[dices_sum] += 1
        return
    for i in range(3):
        dice = i + 1
        get_possible_v2_moves_sum_step(dice, dices_sum, moves_left - 1, end_sums)


def get_possible_v2_moves_sums():
    sums_counter = Counter()
    for i in range(3):
        dice = i + 1
        get_possible_v2_moves_sum_step(dice, 0, 2, sums_counter)
    return sums_counter


def move_v2(position, move_value):
    position = (position + move_value) % POSITIONS_ON_BOARD
    if position == 0:
        position = 10
    return position


def task2_step(positions, positions_counts, scores, win_score, current_player, possible_moves):
    if not all([score < win_score for score in scores]):
        current_player = (current_player + 1) % PLAYERS_COUNT
        result = [0, 0]
        result[current_player] = positions_counts[0] * positions_counts[1]
        return result
    result = [0, 0]
    for possible_move in possible_moves:
        possible_positions = positions.copy()
        possible_positions[current_player] = move_v2(possible_positions[current_player],
                                                     possible_move)
        positions_counts[current_player] *= possible_moves[possible_move]
        scores[current_player] += positions[current_player]
        current_player = (current_player + 1) % PLAYERS_COUNT
        move_result = task2_step(possible_positions, positions_counts.copy(), scores.copy(),
                                 win_score, current_player, possible_moves)
        for i in range(2):
            result[i] += move_result[i]
    return result


def do_task2(positions, win_score):
    possible_moves = get_possible_v2_moves_sums()
    scores = [0 for _ in positions]
    current_player = 0
    players_count = len(positions)
    positions_counts = [1, 1]
    scores = [0, 0]
    return task2_step(positions, positions_counts, scores, win_score, current_player,
                      possible_moves)


WIN_SCORE_1, WIN_SCORE_2 = 1000, 21
result1 = do_task1([int(line[-1]) for line in input_lines], WIN_SCORE_1, POSITIONS_ON_BOARD)
print(f"task1: {result1}")

result2 = do_task2([int(line[-1]) for line in input_lines], WIN_SCORE_2)
print(f"task2: {result2}")
# for result in result2:
#     print(result // 2)
