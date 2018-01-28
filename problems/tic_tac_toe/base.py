"""
Tic Tac Toe board
"""
import itertools
from abc import ABC, abstractmethod
import random

class _Board(ABC):
    """
    Tic Tac Toe Board class
    """

    def __init__(self):
        self.board = [0, 8, 3, 4, 1, 5, 9, 6, 7, 2]

        self.player = []
        self.computer = []
        self.turn = 0

    def check_win(self, move_list: list) -> bool:
        """
        Checks if player/pc has won
        """
        win_moves = filter(
            lambda moves: sum(moves) == 15,
            map(lambda move_list: list(map(self.board.__getitem__, move_list)),\
                filter(lambda move_list: None not in move_list, \
                        itertools.combinations(move_list, 3)))
        )
        return len(list(win_moves)) > 0


    def move_player(self, pos: int) -> bool:
        """
        When player does his move
        """
        if pos not in self.player and pos not in self.computer:
            self.player.append(pos)
            return True
        return False

    @abstractmethod
    def move_comp(self):
        """
        Implement AI logic
        """
        pass

    def __str__(self) -> str:
        string = []
        for row in range(0, 3):
            string.append("| ")
            for col in range(1, 4):
                point = (row * 3) + col
                if point in self.player:
                    string.append("P | ")
                elif point in self.computer:
                    string.append("C | ")
                else:
                    string.append("  | ")
            string.append("\n")
        return ''.join(string)

    def __repr__(self) -> str:
        return self.__str__()

    def get_random_blank(self):
        """
        Gets random blank spot
        """
        check = random.randint(1, 9)
        while check in self.player or check in self.computer:
            check = random.randint(1, 9)
        return check
