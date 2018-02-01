"""
Best First search implementation
"""
from problems.base import BaseProblem

visited = set()


def best_first_search(problem: BaseProblem) -> bool:
    """
    Best first search algo starting

    >>> from problems.test_problem import TProblem
    >>> best_first_search(TProblem(2, 4))
    True
    >>> best_first_search(TProblem(4, 8))
    True
    """
    global visited
    visited = set()

    return best_search_node(problem, problem.start)


def best_search_node(problem: BaseProblem, state) -> bool:
    """
    Best First Search node traversal
    """
    stack = [state]

    while stack.__len__() > 0:
        state = stack.pop()
        if problem.is_goal(state):
            return True

        if state in visited:
            continue

        visited.add(state)

        next_states = sorted(filter(lambda x: x not in visited, problem.get_child_states(state)), key=problem.get_heuristic)
        stack.extend(next_states.__reversed__())

    return False
