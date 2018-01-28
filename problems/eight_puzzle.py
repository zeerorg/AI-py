"""
Eight puzzle problem class
"""

from problems.base import BaseProblem
from helper.gen_help import copy_matrix

class EightPuzzle(BaseProblem):
    """
    Eight puzzle problem
    `start` and `goal` a list of list
    """

    def __init__(self, start, goal):
        super().__init__(start)
        self.goal = goal

    def is_goal(self, state):
        return self.goal == state

    def get_child_states(self, state):
        return [self.shift_down(state),
                self.shift_up(state),
                self.shift_left(state),
                self.shift_right(state)]

    def get_heuristic(self, state):
        ctr = 0
        for row, row_val in enumerate(state):
            for col, _ in enumerate(row_val):
                ctr += int(self.goal[row][col] != state[row][col])
        return ctr

    def shift_up(self, state):
        new_state = copy_matrix(state)

        for row in range(2):
            for col in range(3):
                if new_state[row+1][col] == 0:
                    new_state[row][col], new_state[row+1][col] = 0, new_state[row][col]

        return new_state

    def shift_down(self, state):
        new_state = copy_matrix(state)

        for row in range(1, 3):
            for col in range(3):
                if new_state[row-1][col] == 0:
                    new_state[row][col], new_state[row-1][col] = 0, new_state[row][col]

        return new_state

    def shift_left(self, state):
        new_state = copy_matrix(state)

        for row in range(3):
            for col in range(2):
                if new_state[row][col+1] == 0:
                    new_state[row][col], new_state[row][col+1] = 0, new_state[row][col]

        return new_state

    def shift_right(self, state):
        new_state = copy_matrix(state)

        for row in range(3):
            for col in range(1, 3):
                if new_state[row][col-1] == 0:
                    new_state[row][col], new_state[row][col-1] = 0, new_state[row][col]

        return new_state
    