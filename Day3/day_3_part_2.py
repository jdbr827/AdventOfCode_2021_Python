from typing import List, Tuple

from Day3.day_3_part_1 import convert_binary_to_decimal, BitStr


def format_input(input_filename: str) -> List[BitStr]:
    with open(input_filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


def split_data_by_bit_at_index(data: List[BitStr], idx: int) -> Tuple[List[BitStr], List[BitStr]]:
    """
    Splits the inputted data by the value of the bit at the given index (0s in first output, 1s in second)
    """
    containing_ones = []
    containing_zeros = []
    for data_point in data:
        if data_point[idx] == '0':
            containing_zeros.append(data_point)
        else:
            containing_ones.append(data_point)
    return containing_zeros, containing_ones


def compute_oxygen_generator_rating(input_filename: str) -> int:
    my_data: List[BitStr] = format_input(input_filename)
    n = len(my_data[0])
    idx = 0
    while len(my_data) > 1:
        (containing_zeros, containing_ones) = split_data_by_bit_at_index(my_data, idx)
        my_data = containing_ones if len(containing_ones) >= len(containing_zeros) else containing_zeros
        idx += 1
    return convert_binary_to_decimal(my_data[0])


def compute_c02_scrubber_rating(input_filename: str) -> int:
    my_data: List[BitStr] = format_input(input_filename)
    n = len(my_data[0])
    idx = 0
    while len(my_data) > 1:
        (containing_zeros, containing_ones) = split_data_by_bit_at_index(my_data, idx)
        my_data = containing_ones if len(containing_ones) < len(containing_zeros) else containing_zeros
        idx += 1
    return convert_binary_to_decimal(my_data[0])


def compute_life_support_rating(input_filename: str) -> int:
    oxygen_generator_rating: int = compute_oxygen_generator_rating(input_filename)
    c02_scrubber_rating: int = compute_c02_scrubber_rating(input_filename)
    return oxygen_generator_rating * c02_scrubber_rating


print(compute_oxygen_generator_rating('day_3_small_input.txt') == 23)
print(compute_c02_scrubber_rating('day_3_small_input.txt') == 10)
print(compute_life_support_rating('day_3_small_input.txt') == 230)
print(compute_life_support_rating('day_3_input.txt') == 2845944)
