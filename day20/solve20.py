#!/bin/bash
"""exec" "pyenv" "exec" "python" "$0" "$@"""

import common
import numpy
from common import numpy_matrix

HELP_INFO = [
    "Script is solving task 20 of advent of code 2021",
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


def get_bit_from_input_char(char):
    return 0 if char == '.' else 1


def parse_input(lines):
    key, image = common.get_list_of_groups_divided_empty_line(lines)
    key = [get_bit_from_input_char(bit) for bit in key]
    bin_image = numpy_matrix.get_matrix_from_string_lines(image.split(), int,
                                                          get_bit_from_input_char)
    return key, bin_image


def enhance_image_with_zeros(image, lines_to_enhance):
    size_y, size_x = numpy_matrix.size(image)
    size_y += 2 * lines_to_enhance
    size_x += 2 * lines_to_enhance
    enhanced_image = numpy.zeros((size_y, size_x), int)
    for y, row in enumerate(image):
        for x, item in enumerate(row):
            enhanced_image[y + lines_to_enhance, x + lines_to_enhance] = item
    return enhanced_image


def get_pixel_code(image, y, x, out_of_image_bit):
    neighbours = ""
    size_y, size_x = numpy_matrix.size(image)
    for ny in range(y - 1, y + 2):
        for nx in range(x - 1, x + 2):
            if not (0 <= ny < size_y and 0 <= nx < size_x):
                neighbours += out_of_image_bit
            else:
                neighbours += str(image[ny, nx])
    return neighbours


def apply_enhance_alg(key, image, out_of_image_bit):
    result_image = numpy.zeros_like(image)
    for y, row in enumerate(image):
        for x, item in enumerate(row):
            code = int(get_pixel_code(image, y, x, out_of_image_bit), 2)
            result_image[y, x] = key[code]
    return result_image


def main():
    # numpy.set_printoptions(threshold=numpy.inf)
    key, image = parse_input(input_lines)

    iterations = 50
    image = enhance_image_with_zeros(image, iterations)
    out_of_image_bit = ['0', '1']
    # out_of_image_bit = ['0', '0']  # the one for example data

    for i in range(iterations):
        image = apply_enhance_alg(key, image, out_of_image_bit[i % 2])
        print(i)
    print(image)

    result = sum(sum(image))
    print(f"task1: {result}")


main()
