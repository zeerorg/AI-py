"""
Abstract class for defining problems classes
"""

from abc import ABC, abstractmethod

class BaseProblem(ABC):
    """
    Abstract base class for AI problems
    """

    def __init__(self, start):
        self.start = start

    @abstractmethod
    def get_child_states(self, state):
        """
        Get list of child states from `state` variable
        """
        pass

    @abstractmethod
    def is_goal(self, state):
        """
        Check if `state` is goal
        """
        pass

    @abstractmethod
    def get_heuristic(self, state):
        """
        Get heuristic value of `state`
        more heuristic means more likely
        """
        pass
