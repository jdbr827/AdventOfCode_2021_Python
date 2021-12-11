from typing import List

from util import pad_matrix_with_value

PAD_NUMBER: int = 100


def read_in_matrix(filename) -> List[List[int]]:
    matrix = []
    with open(filename) as f:
        while line := f.readline():
            matrix.append(list(map(int, list(line.strip()))))
    return matrix


print(read_in_matrix('day_11_test_input_1.txt'))


class OctopusMatrix:
    has_flashed: List[List[bool]]

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.padded_matrix = pad_matrix_with_value(matrix, PAD_NUMBER)

    def _increase_energy_level(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                self.padded_matrix[i][j] += 1

    def _flash_octopuses(self) -> int:
        self.has_flashed = [[False for _ in range(self.m + 2)] for _ in range(self.n + 2)]
        flashes = 0
        flashed_this_pass = True
        while flashed_this_pass:
            flashed_this_pass = False
            for i in range(1, self.n + 1):
                for j in range(1, self.m + 1):
                    if self.padded_matrix[i][j] > 9 and not self.has_flashed[i][j]:
                        flashes += 1
                        flashed_this_pass = True
                        self._flash_octopus_at(i, j)

        return flashes

    def _flash_octopus_at(self, i, j):
        self.has_flashed[i][j] = True
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                self.padded_matrix[i + dx][j + dy] += 1

    def _reset_flashed_octopuses(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                if self.has_flashed[i][j]:
                    self.padded_matrix[i][j] = 0
        pass

    def execute_step(self):
        self._increase_energy_level()
        flashes = self._flash_octopuses()
        self._reset_flashed_octopuses()
        return flashes


def count_flashes_over_n_steps(filename, steps):
    octopuses: OctopusMatrix = OctopusMatrix(read_in_matrix(filename))
    flashes = 0
    for _ in range(steps):
        flashes += octopuses.execute_step()
    return flashes


def determine_when_all_octopuses_flash(filename):
    octopuses: OctopusMatrix = OctopusMatrix(read_in_matrix(filename))
    steps = 1
    while (flashes_this_step := octopuses.execute_step()) != 100:
        steps += 1
    return steps


print(count_flashes_over_n_steps('day_11_test_input_1.txt', 10) == 204)
print(count_flashes_over_n_steps('day_11_test_input_1.txt', 100) == 1656)
print(count_flashes_over_n_steps('day_11_input.txt', 100) == 1640)
print(determine_when_all_octopuses_flash('day_11_test_input_1.txt') == 195)
print(determine_when_all_octopuses_flash('day_11_input.txt') == 312)
