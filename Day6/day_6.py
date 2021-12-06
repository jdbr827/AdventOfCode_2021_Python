STARTING_TIMER = 8
RESET_TIMER = 6


def create_initial_lanternfish_frequency_table(filename):
    with open(filename) as f:
        arr = list(map(int, f.read().split(',')))
        freq_arr = [0 for _ in range(STARTING_TIMER + 1)]
        for val in arr:
            freq_arr[val] += 1
        return freq_arr




def move_forward_one_day(freq_arr):
    babys = freq_arr.pop(0)
    freq_arr.append(babys)
    freq_arr[RESET_TIMER] += babys
    return freq_arr


def simulate_lanternfish(filename, days):
    freq_arr = create_initial_lanternfish_frequency_table(filename)
    for _ in range(days):
        freq_arr = move_forward_one_day(freq_arr)
    return sum(freq_arr)


print(simulate_lanternfish('day_6_small_input.txt', 18) == 26)
print(simulate_lanternfish('day_6_small_input.txt', 80) == 5934)
print(simulate_lanternfish('day_6_input.txt', 80) == 386640)