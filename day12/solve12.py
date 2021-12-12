#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
from enum import Enum, auto
from collections import Counter
import numpy

HELP_INFO = [
    "Script is solving task 12 of advent of code 2021",
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


def print_dict_line_by_line(dictionary):
    [print(f"{key}: {value}") for key, value in dictionary.items()]


def print_array_line_by_line(array):
    [print(str(element).strip("[]")) for element in array]


def add_connection(neighbours_list, node1, node2):
    if node1 not in neighbours_list:
        neighbours_list[node1] = []
    if node2 not in neighbours_list:
        neighbours_list[node2] = []
    neighbours_list[node1].append(node2)
    neighbours_list[node2].append(node1)


def create_graph(lines):
    lines = [line.split("-") for line in lines]
    neighbours_list = {}
    for line in lines:
        add_connection(neighbours_list, *line)
    return neighbours_list


def find_paths(graph, node, last_node, visited, parents, paths, path, visited_twice_any):
    if node in visited:
        if visited_twice_any or node == "start":
            return
        else:
            visited_twice_any = True
    path.append(node)
    if node == last_node:
        paths.append(path)
        return
    if 'a' <= node[0] <= 'z':
        visited.append(node)
    for next_node in graph[node]:
        parents[next_node] = node
        find_paths(graph, next_node, last_node, visited.copy(), parents.copy(), paths, path.copy(),
                   visited_twice_any)


def do_task1(lines):
    graph = create_graph(lines)
    paths = []
    find_paths(graph, "start", "end", [], {}, paths, [], True)
    return len(paths)


def do_task2(lines):
    graph = create_graph(lines)
    paths = []
    for node in graph["start"]:
        find_paths(graph, node, "end", ["start"], {}, paths, ["start"], False)
    return len(paths)


result1 = do_task1(input_lines)
result2 = do_task2(input_lines)

print(f"task1: {result1}")
print(f"task2: {result2}")
