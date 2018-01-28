"""
Tests for hill climbing algo (steep and simple)
"""
# pylint: skip-file

from problems.test_problem import TProblem
from algo.simple_hill_climbing import simple_hill_climbing
from algo.steep_hill_climbing import steep_hill_climbing

class NP(TProblem):
    def get_child_states(self, state):
        return [state+1, state+2]

TEST_PROBLEM1 = NP(2, 10)
TEST_PROBLEM2 = TProblem(3, 4)

def test_simple_hill_climb_t1():
    assert simple_hill_climbing(TEST_PROBLEM1)

def test_simple_hill_climb_t2():
    assert not simple_hill_climbing(TEST_PROBLEM2)

def test_steep_hill_climb_t1():
    assert steep_hill_climbing(TEST_PROBLEM1)

def test_steep_hill_climb_t2():
    assert not steep_hill_climbing(TEST_PROBLEM2)
