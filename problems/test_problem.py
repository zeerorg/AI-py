"""
Test problem for testing algos
"""

from problems.base import BaseProblem


class TProblem(BaseProblem):
    """
    Test problem class
    """

    def __init__(self, start, goal):
        super().__init__(start)
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal

    def get_child_states(self, state):
        return [state+2, state*2, state*state, state//4] if state < 1000 else []

    def get_heuristic(self, state):
        return -1 * abs(state - self.goal)


# SOME BASIC TEST SCENARIOS
TEST_PROBLEM1 = TProblem(2, 4)
TEST_PROBLEM2 = TProblem(3, 10)
