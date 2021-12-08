def get_output_digit_strings(filename):
    total_anomaly_digits = 0
    with open(filename) as f:
        while (line := f.readline()):
            output_digits = line.strip().split("|")[1].split(" ")[1:]
            print(output_digits)
            for digit in output_digits:
                if len(digit) in [2, 3, 4, 7]:
                    print(digit)
                    total_anomaly_digits += 1
    return total_anomaly_digits


print(get_output_digit_strings('day_8_small_input.txt') == 26)
print(get_output_digit_strings('day_8_input.txt'))