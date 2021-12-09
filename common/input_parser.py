import sys
import common


def read_lines_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        file.close()
    return lines


def read_script_arguments(argument_keywords):
    argument_to_value_map = {}
    if len(sys.argv) != len(argument_keywords) + 1:
        return argument_to_value_map
    for i in range(len(argument_keywords)):
        argument_to_value_map[argument_keywords[i]] = sys.argv[i + 1]
    return argument_to_value_map


def parse_arguments(arguments_keywords, error_info):
    script_arguments = read_script_arguments(arguments_keywords)
    if common.is_empty(script_arguments):
        common.print_array_line_by_line(error_info)
        return None
    return script_arguments
