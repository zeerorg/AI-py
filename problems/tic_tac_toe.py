"""
Tic Tac Toe board
"""
import itertools
from abc import ABC, abstractmethod

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
            map(lambda move_list: list(map(self.board.__getitem__, move_list)), itertools.combinations(move_list, 3))
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
        Calculates and moves computer
        """
        if self.turn == 0:
            self.computer.append(1)
        elif self.turn == 1 and 5 not in self.player:
            self.computer.append(5)
        elif self.turn == 1:
            self.computer.append(1)
        elif self.turn == 2 and 9 not in self.player:
            self.computer.append(9)
        elif self.turn == 2:
            self.computer.append(3)

        if self.turn < 3:
            return

        for move_pair in itertools.chain(itertools.combinations(self.computer, 2), itertools.combinations(self.player, 2)):
            pair_sum_dif = 15 - sum(map(self.board.__getitem__, move_pair))
            if 0 < pair_sum_dif < 10:
                ind = self.board.index(pair_sum_dif)
                if ind not in self.computer and ind not in self.player:
                    self.computer.append(ind)
                    return

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

class Board_Q2(_Board):

    def move_comp(self):
        super().move_comp()


def start_game():
    """
    Starts the Tic Tac Toe game
    """
    board = Board_Q2()
    choice = input("You will go first ?? (y/N)")
    choice = 0 if choice.lower() == 'y' else 1
    while \
        not board.check_win(board.player) and \
        not board.check_win(board.computer) and \
        board.turn < 9:
        print(board)
        if board.turn % 2 == choice:
            pl_mv = int(input("Enter your move: "))
            while not board.move_player(pl_mv):
                pl_mv = int(input("Incorrect move!! Enter again: "))
        else:
            board.move_comp()
            print("Computer move: {}".format(board.computer[-1]))
        board.turn += 1

    print(board)
    if board.check_win(board.player):
        print("Player Won!!")
    elif board.check_win(board.computer):
        print("Computer Won!!")
    else:
        print("Tied")
            

