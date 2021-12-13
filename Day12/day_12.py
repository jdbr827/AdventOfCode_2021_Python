from collections import defaultdict
from typing import Dict, List

Node = str
Adjacency_List = Dict[Node, List[Node]]


def read_in_edges(filename) -> Adjacency_List:
    adjacency_graph: Adjacency_List = defaultdict(list)
    with open(filename) as f:
        while line := f.readline():
            (v1, v2) = line.strip().split("-")
            adjacency_graph[v1].append(v2)
            adjacency_graph[v2].append(v1)
    return adjacency_graph


def count_cave_paths_recursive(start_node, graph: Adjacency_List, visited_nodes: List[Node]):
    if start_node == 'end': return 1
    if start_node in visited_nodes: return 0
    new_visited_nodes = visited_nodes[:]
    if start_node.islower(): new_visited_nodes.append(start_node)
    return sum([count_cave_paths_recursive(neighbor, graph, new_visited_nodes) for neighbor in graph[start_node]])


def count_cave_paths_from_filename(filename):
    g = read_in_edges(filename)
    return count_cave_paths_recursive('start', g, [])


print(count_cave_paths_from_filename('day_12_small_input.txt') == 10)
print(count_cave_paths_from_filename('day_12_medium_input.txt') == 19)
print(count_cave_paths_from_filename('day_12_large_input.txt') == 226)
print(count_cave_paths_from_filename('day_12_input.txt'))
