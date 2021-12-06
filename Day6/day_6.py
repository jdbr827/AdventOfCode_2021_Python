STARTING_TIMER = 8
RESET_TIMER = 6


def create_initial_lanternfish_frequency_table(filename):
    with open(filename) as f:
        arr = list(map(int, f.read().split(',')))
        print(arr)
        freq_arr = [0 for _ in range(STARTING_TIMER + 1)]
        for val in arr:
            freq_arr[val] += 1
        return freq_arr


print(create_initial_lanternfish_frequency_table('day_6_small_input.txt'))
