"""
Implements steep hill climbing
"""

from problems.base import BaseProblem
from helper.func_prog import compose
from helper.gen_help import add_set


def steep_hill_climbing(problem: BaseProblem) -> bool:
    """
    Main function to start algo
    """
    state = problem.start
    visited = set([state])
    while not problem.is_goal(state):
        next_states = problem.get_child_states(state)

        if compose(len, filter)(visited.__contains__, next_states) > 0:
            return False

        if compose(len, filter)(problem.is_goal, next_states) > 0:
            return True

        state = sorted(next_states, key=problem.get_heuristic)[0]
    return problem.is_goal(state)


def climb_state(problem: BaseProblem, visited: set, state) -> bool:
    """
    Steepest hill climbing
    """
    next_states = sorted(problem.get_child_states(state), key=problem.get_heuristic)
    if state in visited:
        return False

    if compose(len, filter)(problem.is_goal, next_states) > 0:
        return True

    return climb_state(problem, add_set(visited, state), next_states[0])