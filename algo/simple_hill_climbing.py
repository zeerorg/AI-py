"""
Simple hill climbing implemented
"""
from problems.base import BaseProblem


def simple_hill_climbing(problem: BaseProblem):
    """
    Implements simple hill climbing algo
    """
    return hill_climb_node(problem, problem.start)


def hill_climb_node(problem: BaseProblem, state):
    """
    This is a function for single hill climb loop
    """
    if problem.is_goal(state):
        return True

    next_state = get_sorted_child_nodes(problem, state)[-1]
    print(next_state)
    if problem.get_heuristic(state) >= problem.get_heuristic(next_state):
        return False
    return hill_climb_node(problem, next_state)


def get_sorted_child_nodes(problem: BaseProblem, state) -> list:
    """
    gets list of child states sorted by heuristic function
    """
    return sorted(problem.get_child_states(state), key=problem.get_heuristic)
