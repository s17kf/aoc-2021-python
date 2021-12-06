import sys

TAB = "    "


def is_empty(array):
    return len(array) == 0


def get_last_element(array):
    return array[len(array) - 1]


def print_array_line_by_line(array):
    for line in array:
        print(line)


def get_list_of_groups_divided_empty_line(lines, delimiter=" "):
    groups = []
    last_group = ""

    for line in lines:
        if is_empty(line):
            groups.append(last_group.lstrip())
            last_group = ""
            continue
        last_group += delimiter + line
    if last_group != "":
        groups.append(last_group.lstrip())
    return groups


def add_or_increase_for_key(my_dict, key, default_value=1, value_to_increase=1):
    if key in my_dict:
        my_dict[key] += value_to_increase
    else:
        my_dict[key] = default_value
    return my_dict
