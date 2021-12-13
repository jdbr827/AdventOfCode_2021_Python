from collections import defaultdict
from typing import Dict, List


def read_in_edges(filename):
    adjacency_graph: Dict[str, List[str]] = defaultdict(list)
    with open(filename) as f:
        while line := f.readline():
            (v1, v2) = line.strip().split("-")
            adjacency_graph[v1].append(v2)
            adjacency_graph[v2].append(v1)
    return adjacency_graph

print(read_in_edges('day_12_small_input.txt'))

def count_cave_paths_recursive(start_node, adjacency_list, visited_nodes):
    pass
