"""
Test problem for testing algos
"""

from problems.base import BaseProblem

class TestProblem(BaseProblem):
    """
    Test problem class
    """

    def __init__(self, start, goal):
        super().__init__(start)
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal

    def get_child_states(self, state):
        return [state+2, state*2, state*state]

    def get_heuristic(self, state):
        return -1 * abs(state - self.goal)

# SOME BASIC TEST SCENARIOS
TEST_PROBLEM1 = TestProblem(2, 10)
TEST_PROBLEM2 = TestProblem(3, 10)
