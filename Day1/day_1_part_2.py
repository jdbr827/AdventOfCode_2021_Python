"""
Advent Of Code Day 1 Part 2
"""
from typing import List

from Day1.day_1_input_formatter import format_input


def count_increases_sliding_window_3(a: List[int]):
    """
    :param a:
    :return:
    """
    ## A[i] + A[i+1] + A[i+2] < A[i+1] + A[i+2] + A[i+3] <==> A[i] < A[i+3]
    if len(a) < 3:
        return 0
    count = 0
    for i in range(len(a) - 3):
        if a[i + 3] > a[i]:
            count += 1
    return count


print(count_increases_sliding_window_3([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 5)
print(count_increases_sliding_window_3(format_input('day_1_input.txt'))) # 1248
