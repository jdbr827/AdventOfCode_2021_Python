from typing import List


def read_in_matrix(filename):
    matrix = []
    with open(filename) as f:
        while line := f.readline():
            matrix.append(list(map(int, list(line.strip()))))
    return matrix


print(read_in_matrix('day_11_test_input_1.txt'))


def pad_matrix_with_negative_infinitys(matrix: List[List[float]]) -> List[List[float]]:
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        matrix[i].insert(0, -float("inf"))
        matrix[i].append(-float("inf"))
    matrix.insert(0, [-float("inf") for _ in range(m + 2)])
    matrix.append([-float("inf") for _ in range(m + 2)])
    return matrix


def execute_step(matrix):
    # increase energy level of all octopi by 1
    n = len(matrix) - 2
    m = len(matrix[0]) - 2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[i][j] += 1

    has_flashed = [[False for _ in range(m + 2)] for _ in range(n + 2)]

    flashes = 0
    flashed_this_pass = True
    while flashed_this_pass:
        flashed_this_pass = False
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i][j] > 9 and not has_flashed[i][j]:
                    ## Flash
                    flashes += 1
                    flashed_this_pass = True
                    has_flashed[i][j] = True
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            matrix[i + dx][j + dy] += 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if has_flashed[i][j]:
                matrix[i][j] = 0

    return matrix, flashes


def count_flashes_over_n_steps(filename, steps):
    flashes = 0
    matrix = pad_matrix_with_negative_infinitys(read_in_matrix(filename))
    for _ in range(steps):
        (matrix, flashes_this_step) = execute_step(matrix)
        flashes += flashes_this_step
    return flashes

def determine_when_all_octopi_flash(filename):
    matrix = pad_matrix_with_negative_infinitys(read_in_matrix(filename))
    flashes_this_step = 0
    steps = 0
    while flashes_this_step != 100:
        (matrix, flashes_this_step) = execute_step(matrix)
        steps += 1
    return steps



print(count_flashes_over_n_steps('day_11_test_input_1.txt', 10) == 204)
print(count_flashes_over_n_steps('day_11_test_input_1.txt', 100) == 1656)
print(count_flashes_over_n_steps('day_11_input.txt', 100) == 1640)
print(determine_when_all_octopi_flash('day_11_test_input_1.txt') == 195)
print(determine_when_all_octopi_flash('day_11_input.txt'))
