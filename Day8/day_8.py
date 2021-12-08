from collections import defaultdict
from typing import List, Optional


def day_8_part_1(filename):
    total_anomaly_digits = 0
    with open(filename) as f:
        while line := f.readline():
            output_digits = line.strip().split("|")[1].split(" ")[1:]
            for digit in output_digits:
                if len(digit) in [2, 3, 4, 7]:
                    total_anomaly_digits += 1
    return total_anomaly_digits

def sort_chars(input_str):
    return "".join(sorted(input_str))


def get_output_digit_strings(filename):
    sm = 0
    with open(filename) as f:
        while line := f.readline():
            input_digits = line.strip().split("|")[0].split(" ")[:-1]
            output_digits = line.strip().split("|")[1].split(" ")[1:]
            digit_mapping = decode_chars(input_digits)
            sorted_output_digits = list(map(sort_chars, output_digits)) #[sort_chars(x)) for x in output_digits]
            #print(sorted_output_digits, digit_mapping)
            output_numbers = []
            for out_dig in sorted_output_digits:
                for i in range(10):
                    if digit_mapping[i] == out_dig:
                        output_numbers.append(i)
                        break
            assert (len(output_numbers) == 4)
            output_number = sum([10 ** (3 - i) * output_numbers[i] for i in range(4)])
            #print(output_number)
            sm += output_number
    return sm


AVAILABLE_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']



def decode_chars(input_digits):
    digit_mapping: List[Optional[str]] = [None for _ in range(10)]
    input_digits.sort(key=len)

    digit_mapping[1] = sort_chars(input_digits[0])
    digit_mapping[7] = sort_chars(input_digits[1])
    digit_mapping[4] = sort_chars(input_digits[2])
    digit_mapping[8] = sort_chars(input_digits[-1])

    digit_mapping[3] = sort_chars([digit for digit in input_digits[3:6] if all([ch in digit for ch in input_digits[1]])][0])
    digit_mapping[6] = sort_chars([digit for digit in input_digits if len(digit) == 6 and not all([ch in digit for ch in input_digits[1]])][0])
    f = [ch for ch in digit_mapping[6] if ch in digit_mapping[1]][0]
    digit_mapping[2] = sort_chars([digit for digit in input_digits if len(digit) == 5 and f not in digit][0])
    digit_mapping[5] = sort_chars([digit for digit in input_digits if len(digit) == 5 and "".join(sorted(digit)) not in digit_mapping][0])
    digit_mapping[9] = sort_chars([digit for digit in input_digits if len(digit) == 6 and all(ch in digit for ch in digit_mapping[4])][0])
    digit_mapping[0] = sort_chars([digit for digit in input_digits if len(digit) == 6 and "".join(sorted(digit)) not in digit_mapping][0])
    return digit_mapping


print(day_8_part_1('day_8_small_input.txt') == 26)
print(day_8_part_1('day_8_input.txt') == 548)
print(get_output_digit_strings('day_8_small_input.txt') == 61229)
print(get_output_digit_strings('day_8_input.txt') == 1074888)
