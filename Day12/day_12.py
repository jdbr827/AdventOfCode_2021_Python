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


def is_small_cave(node: Node):
    return node.islower()


def count_cave_walks(start_node, graph: Adjacency_List, visited_nodes: List[Node],
                     can_visit_a_node_twice: bool):
    """
    Recursively counts the number of legal walks through a cave from the given start_node to node labelled n
    :param start_node: the starting node of the remainder of the walk
    :param graph: the graph in adjacency list format
    :param visited_nodes: the small caves that have already been visited at least once in the walk
    :param can_visit_a_node_twice: whether you are allowed to visit ONE small cave twice in the walk.
        Can be False because we are not allowing such walks (Part 1),
        OR because a small cave has already been visited at least once (Part 2)
    :return: the number of legal walks remaining from start_node
    """
    if start_node == 'end': return 1
    if start_node in visited_nodes:
        if start_node != 'start' and can_visit_a_node_twice:
            can_visit_a_node_twice = False
        else:
            return 0
    new_visited_nodes = visited_nodes[:]
    if is_small_cave(start_node): new_visited_nodes.append(start_node)
    return sum(
        [count_cave_walks(neighbor, graph, new_visited_nodes, can_visit_a_node_twice) for neighbor in
         graph[start_node]])


def count_cave_paths_from_filename(filename):
    g = read_in_edges(filename)
    return count_cave_walks('start', g, [], False)


def count_cave_paths_from_filename_part_2(filename):
    g = read_in_edges(filename)
    return count_cave_walks('start', g, [], True)


print(count_cave_paths_from_filename('day_12_small_input.txt') == 10)
print(count_cave_paths_from_filename('day_12_medium_input.txt') == 19)
print(count_cave_paths_from_filename('day_12_large_input.txt') == 226)
print(count_cave_paths_from_filename('day_12_input.txt') == 4970)

print(count_cave_paths_from_filename_part_2('day_12_small_input.txt') == 36)
print(count_cave_paths_from_filename_part_2('day_12_medium_input.txt') == 103)
print(count_cave_paths_from_filename_part_2('day_12_large_input.txt') == 3509)
print(count_cave_paths_from_filename_part_2('day_12_input.txt') == 137948)
