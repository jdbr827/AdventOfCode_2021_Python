from collections import defaultdict
from typing import Tuple, Dict


def read_in_points_from_input_line(line) -> Tuple[int, int, int, int]:
    point_pairs = line.strip().split(" -> ")
    points = [[int(a) for a in pt.split(",")] for pt in point_pairs]
    return points[0][0], points[0][1], points[1][0], points[1][1]


def process_line(map, x1, y1, x2, y2):
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            map[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            map[(x, y1)] += 1
    return map


def find_hydraulic_vents(filename):
    vent_freq: Dict[Tuple[int, int], int] = defaultdict(int)
    with open(filename) as f:
        while line := f.readline():
            (x1, y1, x2, y2) = read_in_points_from_input_line(line)
            vent_freq = process_line(vent_freq, x1, y1, x2, y2)
    #print(dict(vent_freq))
    return len([p for p in vent_freq if vent_freq[p] > 1])

print(find_hydraulic_vents('day_5_small_input.txt') == 5)
print(find_hydraulic_vents('day_5_input.txt') == 7644)