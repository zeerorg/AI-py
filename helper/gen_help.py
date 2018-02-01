"""
General Help functions
"""


def copy_matrix(prev):
    """
    Creates copy of a matrix
    """
    new_mat = []
    for r_num, row in enumerate(prev):
        new_mat.append([])
        for c_num, _ in enumerate(row):
            new_mat[-1].append(prev[r_num][c_num])

    return new_mat


def add_set(prev_set: set, ele) -> set:
    """
    Adds new value to set and returns set
    """
    prev_set.add(ele)
    return prev_set


def to_matrix_tuple(matrix: list) -> tuple:
    return tuple(tuple(x) for x in matrix)
