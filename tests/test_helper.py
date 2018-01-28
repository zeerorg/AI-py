"""
Test helper functional programming functions
"""

from helper.func_prog import compose
from helper.monads.iomands import func_print
from helper.gen_help import copy_matrix

def test_compose():
    """
    Test the compose function
    """
    def inc(inp):
        return inp+1

    def square(inp):
        return inp*inp

    def add(inp1, inp2):
        return inp1 + inp2

    assert compose(inc, square, add)(1, 1) == 5
    assert compose(inc)(6) == 7

def test_copy_matrix():
    og_mat = [[1, 2, 3], [4, 5]]
    new_matrix = copy_matrix(og_mat)
    assert new_matrix == og_mat
    new_matrix[0][0] = 0
    assert new_matrix != og_mat
