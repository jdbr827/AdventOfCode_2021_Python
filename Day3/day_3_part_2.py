from typing import List


def format_input(input_filename: str) -> List[str]:
    with open(input_filename) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


def compute_oxygen_generator_rating_binary(input_filename: str):
    my_data: List[str] = format_input(input_filename)
    n = len(my_data[0])
    idx = 0
    while len(my_data) > 1:
        containing_ones = []
        containing_zeros = []
        for data_point in my_data:
            if data_point[idx] == '0':
                containing_zeros.append(data_point)
            else:
                containing_ones.append(data_point)
        if len(containing_ones) >= len(containing_zeros):
            my_data = containing_ones
        else:
            my_data = containing_zeros
        idx += 1
    return my_data[0]



def compute_co2_scrubber_rating(input_filename: str):
    pass

print(compute_oxygen_generator_rating_binary('day_3_small_input.txt') == '10111')
