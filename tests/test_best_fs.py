"""
Writing tests for best first search
"""
from algo.best_first_search import best_first_search
from problems.eight_puzzle import EightPuzzle


def test_8_puz():
    problem = EightPuzzle(((3, 7, 6), (5, 1, 2), (4, 0, 8)), ((5, 3, 6), (7, 0, 2), (4, 1, 8)))
    assert best_first_search(problem)
