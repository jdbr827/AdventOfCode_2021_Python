from typing import List

from Day1.day_1_input_formatter import format_input


def count_increases(a: List[int]) -> int:
    """
    Number of times a value increases from previous value in list a
    :param a:
    :return:
    """
    if a == []:
        return 0
    count = 0
    for i in range(len(a) - 1):
        if a[i + 1] > a[i]:
            count += 1
    return count


print(count_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7)
print(count_increases(format_input('day_1_input.txt'))) # == 1298
