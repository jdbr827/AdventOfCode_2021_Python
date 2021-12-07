
def create_initial_frequency_table(filename):
    with open(filename) as f:
        arr = list(map(int, f.read().split(',')))
        freq_arr = [0 for _ in range(max(arr) + 1)]
        for val in arr:
            freq_arr[val] += 1
        return freq_arr

def find_lowest_fuel_cost(filename):
    freq_arr = create_initial_frequency_table(filename)
    fuel_arr = [i * freq_arr[i] for i in range(len(freq_arr))]
    fuel_used_from_above = sum([i * freq_arr[i] for i in range(len(freq_arr))])
    crabs_below = 0
    fuel_used_from_below = 0
    crabs_above = sum(freq_arr[1:])
    least_fuel_used = fuel_used_from_below + fuel_used_from_above
    for i in range(1, len(freq_arr)):
        crabs_below += freq_arr[i - 1]
        # fuel_used_from_below = sum([abs(j-i) * ])
        crabs_above -= freq_arr[i]
        # fuel_used_from_above -= crabs_above
        # total_fuel = fuel_used_from_below + fuel_used_from_above
        total_fuel = sum([abs(i-j) * freq_arr[j] for j in range(len(freq_arr))])
        least_fuel_used = min(least_fuel_used, total_fuel)
    return least_fuel_used

# print(create_initial_frequency_table('day_7_small_input.txt'))
print(find_lowest_fuel_cost('day_7_small_input.txt') == 37)
print(find_lowest_fuel_cost('day_7_input.txt'))