"""
Tic tac toe ques 1 module
"""
import itertools

from problems.tic_tac_toe.base import _Board


class BoardQ1(_Board):
    """
    Question 1 implementation of Tic Tac Toe
    """

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
        elif self.turn == 3 and self.will_win(self.player) != -1:
            self.computer.append(self.will_win(self.player))
        elif self.turn == 3:
            self.computer.append(self.make_2())
        elif self.turn == 4:
            if self.win_or_block():
                pass
            elif 7 not in self.player and 7 not in self.computer:
                self.computer.append(7)
            else:
                self.computer.append(3)
        elif self.turn == 5:
            if self.win_or_block():
                pass
            else:
                self.computer.append(self.make_2())
        else:
            if self.win_or_block():
                pass
            else:
                self.computer.append(self.get_any_blank())

        # print(self.computer[-1])

    def get_any_blank(self):
        """
        Returns a blank position
        """
        for point in range(1, 10):
            if point not in self.player and point not in self.computer:
                return point

    def win_or_block(self) -> bool:
        """
        Moves computer to win or to block player
        """
        if self.will_win(self.computer) != -1:
            self.computer.append(self.will_win(self.computer))
            return True
        elif self.will_win(self.player) != -1:
            self.computer.append(self.will_win(self.player))
            return True
        return False

    def make_2(self) -> int:
        """
        Return 5 or (2, 4, 6, 8)
        """
        for point in [5, 2, 4, 6, 8]:
            if point not in self.player and point not in self.computer:
                return point

    def will_win(self, move_list: list) -> int:
        """
        Check next move to make to win from move_list
        """
        for move in filter(lambda move_list: None not in move_list, itertools.combinations(move_list, 2)):
            pair_sum_dif = 15 - sum(map(self.board.__getitem__, move))
            if 0 < pair_sum_dif < 10:
                ind = self.board.index(pair_sum_dif)
                if ind not in self.computer and ind not in self.player:
                    return ind
        return -1


def start_game(board_class):
    """
    Starts the Tic Tac Toe game
    """
    board = board_class()
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
