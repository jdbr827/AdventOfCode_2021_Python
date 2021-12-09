from collections import defaultdict
from typing import List, Tuple

from Day9.unionfind import UnionFindSize, UnionFind


def read_in_space_time_points(filename) -> List[Tuple[int, int, int, int]]:
    points = []
    with open(filename) as f:
        while line := f.readline():
            points.append(tuple(map(int, line.split(","))))
    return points


def manhattan_distance(point1, point2):
    total_dist = 0
    for i in range(4):
        total_dist += abs(point1[i] - point2[i])
    return total_dist


def count_constellations(points: List[Tuple[int, int, int, int]]) -> int:
    n = len(points)
    constellation_uf = UnionFind(lambda a, b: min(a, b))
    for i in range(n):
        constellation_uf.makeset(i)
        for j in range(i):
            if manhattan_distance(points[i], points[j]) <= 3:
                constellation_uf.union(i, j)
    constellation_vals = defaultdict(int)
    for i in range(n):
        constellation_vals[constellation_uf.find(i)] += 1
    return len(constellation_vals.keys())


print(read_in_space_time_points('2018_day_25_small_input_1.txt'))
print(count_constellations(read_in_space_time_points('2018_day_25_small_input_1.txt')) == 2)
print(count_constellations(read_in_space_time_points('2018_day_25_input.txt')))
