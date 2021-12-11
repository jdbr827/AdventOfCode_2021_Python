from typing import List, TypeVar, Generic, Type

T = TypeVar("T")


def pad_matrix_with_value(matrix: List[List[T]], value: T) -> List[List[T]]:
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        matrix[i].insert(0, value)
        matrix[i].append(value)
    matrix.insert(0, [value for _ in range(m + 2)])
    matrix.append([value for _ in range(m + 2)])
    return matrix
