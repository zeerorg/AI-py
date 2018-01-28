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
