from collections import defaultdict
from typing import List, Optional


def get_output_digit_strings(filename):
    total_anomaly_digits = 0
    sm = 0
    with open(filename) as f:
        while (line := f.readline()):
            input_digits = line.strip().split("|")[0].split(" ")[:-1]
            output_digits = line.strip().split("|")[1].split(" ")[1:]
            #print(input_digits)
            digit_mapping = decode_chars(input_digits)
            for digit in output_digits:
                if len(digit) in [2, 3, 4, 7]:
                    # print(digit)
                    total_anomaly_digits += 1
            sorted_output_digits = ["".join(sorted(x)) for x in output_digits]
            print(sorted_output_digits, digit_mapping)
            output_numbers = []
            for out_dig in sorted_output_digits:
                for i in range(10):
                    if digit_mapping[i] == out_dig:
                        output_numbers.append(i)
                        break
            #print(output_numbers)
            assert(len(output_numbers) == 4)
            output_number = sum([10**(3-i) * output_numbers[i] for i in range(4)])
            print(output_number)
            sm += output_number
    print(sm)
    return total_anomaly_digits


AVAILABLE_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def decode_chars(input_digits):
    char_mapping = defaultdict(None)
    digit_mapping : List[Optional[str]] = [None for _ in range(10)]
    char_freq_table = defaultdict(int)
    for digit in input_digits:
        for ch in digit:
            char_freq_table[ch] += 1
    input_digits.sort(key=len)
    digit_mapping[1] = "".join(sorted(input_digits[0]))
    digit_mapping[7] = "".join(sorted(input_digits[1]))
    digit_mapping[4] = "".join(sorted(input_digits[2]))
    digit_mapping[8] = "".join(sorted(input_digits[-1]))
    char_mapping['a'] = [ch for ch in digit_mapping[7] if ch not in digit_mapping[1]][0]
    digit_mapping[3] = "".join(sorted([digit for digit in input_digits[3:6] if all([ch in digit for ch in input_digits[1]])][0]))
    digit_mapping[6] = "".join(sorted([digit for digit in input_digits if len(digit) == 6 and not all([ch in digit for ch in input_digits[1]])][0]))
    char_mapping['f'] = [ch for ch in digit_mapping[6] if ch in digit_mapping[1]][0]
    digit_mapping[2] = "".join(sorted([digit for digit in input_digits if len(digit) == 5 and char_mapping['f'] not in digit][0]))
    digit_mapping[5] = "".join(sorted([digit for digit in input_digits if len(digit) == 5 and "".join(sorted(digit)) not in digit_mapping][0]))
    digit_mapping[9] = "".join(sorted([digit for digit in input_digits if len(digit) == 6 and all(ch in digit for ch in digit_mapping[4])][0]))
    digit_mapping[0] = "".join(sorted([digit for digit in input_digits if len(digit) == 6 and "".join(sorted(digit)) not in digit_mapping][0]))
    # print(input_digits)
    # print(digit_mapping)
    # print(char_mapping)
    return digit_mapping







print(get_output_digit_strings('day_8_small_input.txt') == 26)
print(get_output_digit_strings('day_8_input.txt'))
