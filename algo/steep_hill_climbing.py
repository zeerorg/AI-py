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
    return climb_state(problem, set(), problem.start)


def climb_state(problem: BaseProblem, visited: set, state) -> bool:
    """
    Steepest hill climbing node
    """
    next_states = sorted(problem.get_child_states(state), key=problem.get_heuristic)
    if state in visited:
        return False

    if compose(len, list, filter)(problem.is_goal, next_states) > 0:
        return True

    return climb_state(problem, add_set(visited, state), next_states[-1])
