from collections import defaultdict
from typing import List, Dict, Tuple
import unionfind


def read_in_matrix(filename) -> List[List[int]]:
    matrix = []
    with open(filename) as f:
        while line := f.readline():
            matrix.append(list(map(int, list(line.strip()))))
    return matrix


a = read_in_matrix('day_9_small_input.txt')


def pad_matrix_with_infinitys(matrix: List[List[float]]) -> List[List[float]]:
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        matrix[i].insert(0, float("inf"))
        matrix[i].append(float("inf"))
    matrix.insert(0, [float("inf") for _ in range(m + 2)])
    matrix.append([float("inf") for _ in range(m + 2)])
    return matrix


b = pad_matrix_with_infinitys(a)


def find_low_points(padded_matrix: List[List[float]]) -> List[float]:
    n = len(padded_matrix) - 2
    m = len(padded_matrix[0]) - 2
    low_points = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if padded_matrix[i][j] < min(padded_matrix[i + 1][j], padded_matrix[i - 1][j], padded_matrix[i][j - 1],
                                         padded_matrix[i][j + 1]):
                low_points.append(padded_matrix[i][j])
    return low_points


def risk_level(filename) -> int:
    matrix = pad_matrix_with_infinitys(read_in_matrix(filename))
    low_points = find_low_points(matrix)
    return sum([p + 1 for p in low_points])


# print(risk_level('day_9_small_input.txt') == 15)
print(risk_level('day_9_input.txt'))


def find_basins(padded_matrix: List[List[float]]) -> Dict[Tuple[int, int], int]:
    """

    :param padded_matrix:
    :return: basin_matrix: where keys are locations of lowest points of basins, and values are sizes of basins
    """
    basin_finder = unionfind.UnionFindSize(lambda p1, p2: min((p1, p2), key=lambda p: padded_matrix[p[0]][p[1]]))

    n = len(padded_matrix) - 2
    m = len(padded_matrix[0]) - 2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if padded_matrix[i][j] != 9:
                basin_finder.makeset((i, j))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if padded_matrix[i][j] != 9:
                for nbr in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                    if padded_matrix[nbr[0]][nbr[1]] < 9:
                        basin_finder.union((i, j), nbr)
    freq_table = defaultdict(int)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if padded_matrix[i][j] != 9:
                freq_table[basin_finder.find((i, j))] += 1
    return freq_table


def product_of_three_largest_basins(filename):
    basins: Dict[Tuple[int, int], int] = dict(find_basins(pad_matrix_with_infinitys(read_in_matrix(filename))))
    sizes: List[int] = list(basins.values())
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


print(product_of_three_largest_basins('day_9_small_input.txt') == 1134)
print(product_of_three_largest_basins('day_9_input.txt'))
# if padded_matrix[i][j] < min(padded_matrix[i+1][j], padded_matrix[i-1][j], padded_matrix[i][j-1], padded_matrix[i][j+1]):
